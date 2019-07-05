"""
Bill weinman
"""
import re

file1 = 'D:\\Work\\Yupana\\ATT\\SRT.BAU\\NCAL_SRT\\LTE\\CIQ\\SFO_LTE_RNDCIQ_REV_358_02202018\\CIQ_ENBINFO_NCAL.txt'
file2 = 'D:\\Work\\Yupana\\ATT\\SRT.BAU\\NCAL_SRT\\LTE\\CIQ\\SFO_LTE_RNDCIQ_REV_358_02202018\\CIQ_LTELTE_NCAL.txt'
# siteid = 'CCL09633'

def main(siteid):
	try:
		pattern = re.compile(siteid)
		for line in readfile(file2):
			# print(line.rstrip())
			sline = line.rstrip()
			m = re.search(pattern, sline)
			if m:
				cell = line.split('#')[0]
				earfcndl = line.split('#')[1]
				print('EUtranCellFDD: ' + cell)
				print('earfcnDl: ' + earfcndl)
	except IOError as e:
		print('Cannot read file:\n', e)
	except ValueError as e:
		print('bad filename:\n', e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh
	else:
		raise ValueError('Filename must end with .txt')

def test_main():
	main('CCL09633')

if __name__ == '__main__':
	test_main()
