"""
Bill weinman
"""

import re

file1 = 'D:\\Work\\Yupana\\ATT\\SRT.BAU\\NCAL_SRT\\LTE\\CIQ\\SFO_LTE_RNDCIQ_REV_358_02202018\\CIQ_ENBINFO_NCAL.txt'
file2 = 'D:\\Work\\Yupana\\ATT\\SRT.BAU\\NCAL_SRT\\LTE\\CIQ\\SFO_LTE_RNDCIQ_REV_358_02202018\\CIQ_LTELTE_NCA.txt'

# -----------------------
# Search
# -----------------------
# with open(file2) as f:
# 	for line in f:
# 		# print(line.rstrip())
# 		sline = line.rstrip()
# 		m = re.search(r'CCL09633', sline)
# 		if m:
# 			print(sline)
# 			print(sline[:m.start()] + sline[m.end():])

siteid = 'CCL09633'

try:
	with open(file2, 'r') as f:
		pattern = re.compile(siteid)
		for line in f:
			# print(line.rstrip())
			sline = line.rstrip()
			m = re.search(pattern, sline)
			if m:
				cell = line.split('#')[0]
				earfcndl = line.split('#')[1]
				print('EUtranCellFDD: ' + cell)
				print('earfcnDl: ' + earfcndl)
except IOError as e:
	print('Could not open the file: \n', e)


