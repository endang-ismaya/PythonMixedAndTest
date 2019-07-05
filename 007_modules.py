"""
Modules
"""

from time import sleep, asctime
import sys
import csv

# print(asctime())
# sleep(5)
# print(asctime())
#
# for path in sys.path:
# 	print(path)


csv_fileinfo = "D:\\Work\\Yupana\\Yupana.Software\\new_methodology\Parser\\Takbir Parsing\\output\\CCL00027_CellInfo.csv"

# with open(csv_file) as f:
# 	reader = csv.reader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
# 	for row in reader:
# 		print(row)

# result = []
# with open(csv_file) as f:
# 	reader = csv.reader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
# 	for row in reader:
# 		# print(row)
# 		result.append(row)
# 	print(result)

# result = []
# with open(csv_fileinfo) as f:
# 	reader = csv.DictReader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
# 	for row in reader:
# 		print(row['SiteName'], row['EutranCellFDD'])


cell_infos = {}
def read_csv_file(csv_file):
	with open(csv_file) as f:
		reader = csv.DictReader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			# print(row['SiteName'], row['EutranCellFDD'])
			cell_infos[row['EutranCellFDD']] = [row['SiteName'], row['SectorCarrier'], row['EarfcnDl']]


def get_bandcategory_from_csvfile_source_fdd(csv_file, fdd):
	with open(csv_file) as f:
		reader = csv.DictReader(f, delimiter='#', quotechar='#', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			if row['EutranCellFDD'] == fdd:
				return row['BandCategory']


# cell_list = ['CCL00027_7A_1', 'CCL00027_7B_1', 'CCL00027_7C_1']
# read_csv_file(csv_fileinfo)
#
# for cell in cell_list:
# 	if cell in cell_infos.keys():
# 		print('{0:15} {1:20} {2:8}'.format(cell, cell_infos[cell][1], cell_infos[cell][2]))

myCategory = get_bandcategory_from_csvfile_source_fdd(csv_fileinfo, 'CCL00027_7C_1')
print(myCategory)
