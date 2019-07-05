"""
Read CIQ parsed file
"""
import csv

enbinfo = r'D:\Work\Yupana\ATT\SRT.BAU\NCAL_SRT\LTE\CIQ\SFO_LTE_RNDCIQ_REV_361_03262018\CIQ_ENBINFO_NCAL.txt'
eutran = r'D:\Work\Yupana\ATT\SRT.BAU\NCAL_SRT\LTE\CIQ\SFO_LTE_RNDCIQ_REV_361_03262018\CIQ_EUTRANPARAMETER_NCAL.txt'

# with open(enbinfo) as f:
# 	reader = csv.reader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
# 	for row in reader:
# 		print(row)

# enbids = {}
# rbstypes = {}
# tacs = {}
# with open(enbinfo) as f:
# 	reader = csv.DictReader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
# 	for row in reader:
# 		# print(row)
# 		if row['eNodeB Name'] == 'CVL01803':
# 			print(row)
# 			enbids['CVL01803'] = row['eNBId']
# 			rbstypes['CVL01803'] = row['RBS type']
# 			tacs['CVL01803'] = row['tac']
#
# print('SiteId: ' + 'CVL01803')
# print('eNBId: ' + enbids.get('CVL01803', '_NA_'))
# print('RBS.Type: ' + rbstypes.get('CVL01803', '_NA_'))
# print('tac: ' + tacs.get('CVL01803', '_NA_'))

# OrderedDict([('eNodeB Name', 'CVL01803'), ('eNBId', '671803'), ('RBS type', 'RBS6202'), ('tac', '36108')])

def get_reader(siteid):
	with open(enbinfo) as f:
		reader = csv.DictReader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			if row['eNodeB Name'] == siteid:
				return row

xrow = get_reader('CVL01803')
print(xrow['eNBId'])


def get_reader(enbid):
	rows = []
	with open(eutran) as f:
		reader = csv.DictReader(f, delimiter='#', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			if row['eNBId'] == enbid:
				rows.append(row)
		return rows

qrows = get_reader('661732')
# print(qrows)
for qrow in qrows:
	if qrow['EutranCellFDDId'] == 'CCL01732_7C_1':
		print(qrow['noOfRxAntennas'])
