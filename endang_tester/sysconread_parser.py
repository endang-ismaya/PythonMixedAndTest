"""
SysCon Reader v1.0.0
Created: 4/9/2018
Update: -
"""
import os
import re
from endang_tester import kget_db_class

srtcheck_folder = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe'
srtcheck1 = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe\CVL01207_SRT_CHECK.log'
srtcheck2 = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe\CVL07209R_SRT_CHECK.log'
dbpath = \
	r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe\20180408_134149_CVL01207_CVL07209R_TESTER.db'

# 'siteid', 'mo', 'moclass', 'parameter', 'currentvalue', 'source_element', 'target_element'

class SysconReader:

	def __init__(self, path_folder, final_srtdb):
		self._path_folder = path_folder
		self._final_srtdb = final_srtdb
		self._parsed_data = []

	@property
	def get_srtcheckfiles(self):
		srtcheckfiles = []
		for srtcheck_file in os.listdir(self._path_folder):
			if srtcheck_file.endswith('.log') and 'SRT_CHECK' in srtcheck_file:
				srt_chk_file = os.path.join(self._path_folder, srtcheck_file)
				srtcheckfiles.append(srt_chk_file)
		return srtcheckfiles

	@property
	def get_syscon_data(self):
		return self._parsed_data

	def read_srtcheck(self):
		for srtcheck_file in self.get_srtcheckfiles:
			sitename = 'siteid'
			with open(srtcheck_file) as f:
				for line in f:
					xline = line.rstrip()
					m0 = re.match(r'^\$sitename\s=\s(\w+)', xline)
					m1 = re.match(r'^\d+:\d+.*', xline)

					if m0:
						sitename = m0.group(1)
						# print(sitename)
					elif m1:
						self.generate_parsed_data(sitename, xline)
						break

	def generate_parsed_data(self, sitename, xline):
		# print(sitename, xline)
		for line in str(xline).split(','):
			parameter = line.split(':')[0]
			value = line.split(':')[1]
			data = [sitename, '/cm/sysconread', 'SystemConstants', parameter, value, '/cm/sysconread', '']
			self._parsed_data.append(data)

def main():
	syscon = SysconReader(srtcheck_folder, dbpath)
	syscon.read_srtcheck()

	# for data in syscon.get_syscon_data:
	# 	print(data)

	if len(syscon.get_syscon_data) > 0:
		insert_to_db = kget_db_class.CreateParsedDb(syscon.get_syscon_data, dbpath)
		insert_to_db.insert_db()

if __name__ == '__main__':
	main()
