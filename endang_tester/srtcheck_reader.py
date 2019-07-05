"""
SRT Check Reader v1.0.0
Created: 4/2/2018
Update: -
"""
import csv
import os
import re
import copy
from endang_tester import srtcheck_dbcreate as db
import datetime

class SrtCheckReader:

	__srt_check_result = []
	__site_naming = ''
	__csv_filename = 'Invxr_Profile.csv'

	def __init__(self, path_folder, print_type):
		self._path_folder = path_folder
		self._print_type = print_type
		self.create_filenaming()

	def get_srt_check_result(self):
		return self.__srt_check_result

	@property
	def get_sqliltedb_naming(self):
		sdate = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_")
		return sdate + self.__site_naming + 'srtdb.db'

	@property
	def get_csv_filename(self):
		return self.__csv_filename

	def create_filenaming(self):
		for srtcheck_file in os.listdir(self._path_folder):
			if srtcheck_file.endswith('.log') and 'SRT_CHECK' in srtcheck_file:
				srt_chk_file = os.path.join(self._path_folder, srtcheck_file)
				with open(srt_chk_file) as f:
					for line in f:
						m1 = re.match(r'^\$sitename\s=\s(\w+)', line)
						if m1:
							sitename = m1.group(1)
							self.__site_naming += sitename + '_'
							break

	def create_invxr(self):
		invxr_fdds = []
		rfbrances = []
		linkbudgets = []

		for srtcheck_file in os.listdir(self._path_folder):
			if srtcheck_file.endswith('.log') and 'SRT_CHECK' in srtcheck_file:
				srt_chk_file = os.path.join(self._path_folder, srtcheck_file)
				# print(srt_chk_file)
				auxpiu = 0
				lnh = 1
				board = 2
				rf = 3
				sitename = 'siteid'
				with open(srt_chk_file) as f:
					for line in f:
						m0 = re.match(r'^AuxPiu.*;LNH.*PCI.*', line)
						m1 = re.match(r'^\$sitename\s=\s(\w+)', line)
						m2 = re.findall(r'RRU.*;.*FDD=(\w+).*FDD=(\w+)', line)
						m3 = re.findall(r'RRU.*;.*FDD=(\w+).*', line)
						m_rfbranch_bbu = re.match(
							r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*SectorEquipment.*FieldReplaceableUnit=([\w-]+),RfPort=(\w)',
							line)
						m_rfbranch_dus = re.match(
							r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*SectorEquipment.*AuxPlugInUnit=([\w-]+),DeviceGroup=ru,RfPort=(\w)',
							line)
						m_linkbudget = re.match(
							r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*;i\[\d+\]\s=([\d\s]+).*=([\d\s]+).*=([\d\s]+).*([\d\s]+)',
							line)
						if m1:
							sitename = m1.group(1)
						elif m0:
							arrs = line.split(';')
							for i, arr in enumerate(arrs):
								# print(idx, arr)
								if arr.rstrip().lower() == 'AuxPiu'.lower():
									auxpiu = i
								elif arr.rstrip().lower() == 'LNH'.lower():
									lnh = i
								elif arr.rstrip().lower() == 'BOARD'.lower():
									board = i
								elif arr.rstrip().lower() == 'RF'.lower():
									rf = i
						elif m2:
							arrs = line.split(';')
							invxr_fdds.append(
								[
									sitename, m2[0][0], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()),
									str(arrs[board].strip()), str(arrs[rf].strip())
								]
							)
							invxr_fdds.append(
								[
									sitename, m2[0][1], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()),
									str(arrs[board].strip()), str(arrs[rf].strip())
								]
							)
						elif m3:
							arrs = line.split(';')
							invxr_fdds.append(
								[sitename, m3[0], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()), str(arrs[board].strip()),
									str(arrs[rf].strip())])
						elif m_rfbranch_bbu:
							# print(m_rfbranch1.group(1), m_rfbranch1.group(2), m_rfbranch1.group(3))
							rfbrances.append(
								[m_rfbranch_bbu.group(1), m_rfbranch_bbu.group(2), m_rfbranch_bbu.group(3)])
						elif m_rfbranch_dus:
							# print(m_rfbranch1.group(1), m_rfbranch1.group(2), m_rfbranch1.group(3))
							rfbrances.append(
								[m_rfbranch_dus.group(1), m_rfbranch_dus.group(2), m_rfbranch_dus.group(3)])
						elif m_linkbudget:
							# print(
							# 	m_linkbudget.group(1), m_linkbudget.group(2), m_linkbudget.group(3), m_linkbudget.group(4),
							# 	m_linkbudget.group(4)
							# )
							linkbudgets.append(
								[
									m_linkbudget.group(1), m_linkbudget.group(2), m_linkbudget.group(3),
									m_linkbudget.group(4), m_linkbudget.group(4)
								]
							)

		# for lb in linkbudgets:
		# 	print(lb)

		# for fdd in invxr_fdds:
		# 	print(fdd)

		srt_checks = []
		for x in invxr_fdds:
			x_siteid = x[0]
			x_fdd = x[1]
			x_rru = x[2]
			x_bxp = x[3]
			x_board = x[4]
			x_rf = x[5]
			# print(x)
			for y in rfbrances:
				y_branch = y[0]
				y_rru = y[1]
				y_rf = y[2]
				# print(y)
				if x_rru.lower() == y_rru.lower() and x_rf.lower() == y_rf.lower():
					for z in linkbudgets:
						z_branch = z[0]
						z_dlattenuation = z[1].strip().replace(' ', ':')
						z_dltrafficdelay = z[2].strip().replace(' ', ':')
						z_ulattenuation = z[3].strip().replace(' ', ':')
						z_ultrafficdelay = z[4].strip().replace(' ', ':')
						# print(z)
						if y_branch.lower() == z_branch.lower():
							srt_checks.append(
								[
									x_siteid, x_fdd, x_rru, x_rf, x_bxp, x_board, y_branch, z_dlattenuation, z_dltrafficdelay,
									z_ulattenuation, z_ultrafficdelay
								]
							)
							break

		self.__srt_check_result = copy.deepcopy(srt_checks)
		srt_checks.insert(
			0, [
				'siteid', 'eutrancellfdd', 'fru', 'rf', 'lnh', 'board', 'branch', 'dlattenuation', 'dltrafficdelay',
				'ulattenuation', 'ultrafficdelay'
			]
		)

		if self._print_type == 1 or self._print_type == 3:
			# print to csv
			file_name = os.path.join(self._path_folder, self.__csv_filename)
			if os.path.exists(file_name):
				os.remove(file_name)
			with open(file_name, 'w', newline='') as fp:
				a = csv.writer(fp, delimiter=',')
				a.writerows(srt_checks)
			print('file save as: ' + file_name)

		if self._print_type == 2 or self._print_type == 3:
			# print to sqlite
			file_db_fullpath = os.path.join(self._path_folder, self.get_sqliltedb_naming)
			cr_invxr = db.CreateSRTCheckDb(self.__srt_check_result, file_db_fullpath)
			cr_invxr.create_db()
			cr_invxr.insert_db()
