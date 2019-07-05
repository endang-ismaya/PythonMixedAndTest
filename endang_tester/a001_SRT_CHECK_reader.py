"""
SRT_CHECK Reader
"""
# import os
import re

file_dus = r'C:\cygwin\home\endang.ismaya\ts_esrtlog\GeSRT\DUS_CVL02491_CVL09079R_CVL02295\CVL09079R_SRT_CHECK.log'
file_bbu = r'C:\cygwin\home\endang.ismaya\ts_esrtlog\GeSRT\FirstNet_IDLe\CVL07209R_SRT_CHECK.log'

# for srt_check in os.listdir(path):
# 	if srt_check.endswith('.log') and 'SRT_CHECK' in srt_check:
# 		srt_chk_file = os.path.join(path, srt_check)
# 		with open(srt_chk_file) as f:
# 			for line in f:
# 				print(line.rstrip())

file_1 = r'C:\cygwin\home\endang.ismaya\ts_esrtlog\GeSRT\FirstNet_IDLe\CVL01207_SRT_CHECK.log'
file_2 = r'C:\cygwin\home\endang.ismaya\ts_esrtlog\GeSRT\FirstNet_IDLe\CVL07209R_SRT_CHECK.log'

auxpiu = 0
lnh = 1
board = 2
rf = 3
sector = 7

invxr_fdds = []
rfbranches = []
linkbudgets = []
with open(file_2) as f:
	for line in f:
		m0 = re.match(r'^AuxPiu.*;LNH.*PCI.*', line)
		m1 = re.match(r'^\$sitename\s=\s(\w+)', line)
		m2 = re.findall(r'RRU.*;.*FDD=(\w+).*FDD=(\w+)', line)
		m3 = re.findall(r'RRU.*;.*FDD=(\w+).*', line)
		m_rfbranch_bbu = re.match(
			r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*SectorEquipment.*FieldReplaceableUnit=([\w-]+),RfPort=(\w)',
			line
		)
		m_rfbranch_dus = re.match(
			r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*SectorEquipment.*AuxPlugInUnit=([\w-]+),DeviceGroup=ru,RfPort=(\w)',
			line
		)
		m_linkbudget = re.match(
			r'^(AntennaUnitGroup=\w+,RfBranch=\w+)\s?.*;i\[\d+\]\s=([\d\s]+).*=([\d\s]+).*=([\d\s]+).*([\d\s]+)', line
		)
		if m1:
			sitename = m1.group(1)
			print(sitename)
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
		if m2:
			arrs = line.split(';')
			invxr_fdds.append(
				[
					m2[0][0], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()),
					str(arrs[board].strip()), str(arrs[rf].strip())
				]
			)
			invxr_fdds.append(
				[
					m2[0][1], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()), str(arrs[board].strip()),
					str(arrs[rf].strip())
				]
			)
		elif m3:
			arrs = line.split(';')
			invxr_fdds.append(
				[
					m3[0], str(arrs[auxpiu].strip()), str(arrs[lnh].strip()), str(arrs[board].strip()),
					str(arrs[rf].strip())
				]
			)
		elif m_rfbranch_bbu:
			# print(m_rfbranch1.group(1), m_rfbranch1.group(2), m_rfbranch1.group(3))
			rfbranches.append(
				[m_rfbranch_bbu.group(1), m_rfbranch_bbu.group(2), m_rfbranch_bbu.group(3)]
			)
		elif m_rfbranch_dus:
			# print(m_rfbranch1.group(1), m_rfbranch1.group(2), m_rfbranch1.group(3))
			rfbranches.append(
				[m_rfbranch_dus.group(1), m_rfbranch_dus.group(2), m_rfbranch_dus.group(3)]
			)
		elif m_linkbudget:
			# print(
			# 	m_linkbudget.group(1), m_linkbudget.group(2), m_linkbudget.group(3), m_linkbudget.group(4),
			# 	m_linkbudget.group(4)
			# )
			linkbudgets.append(
				[
					m_linkbudget.group(1), m_linkbudget.group(2), m_linkbudget.group(3), m_linkbudget.group(4),
					m_linkbudget.group(4)
				]
			)

# for fdd in invxr_fdds:
# 	print(fdd)

# for y in rfbranches:
# 	print(y)

# for lb in linkbudgets:
# 	print(lb)

# srt_checks = []
# for x in invxr_fdds:
# 	x_fdd = x[0]
# 	x_rru = x[1]
# 	x_bxp = x[2]
# 	x_board = x[3]
# 	x_rf = x[4]
# 	# print(x)
# 	for y in rfbrances:
# 		y_branch = y[0]
# 		y_rru = y[1]
# 		y_rf = y[2]
# 		if x_rru.lower() == y_rru.lower() and \
# 			x_rf.lower() == y_rf.lower():
# 			for z in linkbudgets:
# 				z_branch = z[0]
# 				z_dlAttenuation = z[1].strip().replace(' ', ':')
# 				z_dlTrafficDelay = z[2].strip().replace(' ', ':')
# 				z_ulAttenuation = z[3].strip().replace(' ', ':')
# 				z_ulTrafficDelay = z[4].strip().replace(' ', ':')
# 				if y_branch.lower() == z_branch.lower():
# 					srt_checks.append(
# 						[
# 							x_fdd, x_rru, x_rf, x_bxp, x_board, y_branch, z_dlAttenuation, z_dlTrafficDelay,
# 							z_ulAttenuation, z_ulTrafficDelay
# 						]
# 					)
#
# for item in srt_checks:
# 	print(item)

