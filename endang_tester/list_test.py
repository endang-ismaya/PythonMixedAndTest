from collections import Counter
# elist = [
# 	['CVL01207', 'SectorEquipmentFunction=1'],
# 	['CVL01207', 'SectorEquipmentFunction=2'],
# 	['CVL01207', 'SectorEquipmentFunction=3'],
# 	['CVL01207', 'SectorEquipmentFunction=4'],
# 	['CVL01207', 'SectorEquipmentFunction=5'],
# 	['CVL01207', 'SectorEquipmentFunction=6'],
# 	['CVL01207', 'SectorEquipmentFunction=10'],
# 	['CVL01207', 'SectorEquipmentFunction=11'],
# 	['CVL01207', 'SectorEquipmentFunction=12'],
# 	['CVL07209R', 'SectorEquipmentFunction=7'],
# 	['CVL07209R', 'SectorEquipmentFunction=8'],
# 	['CVL07209R', 'SectorEquipmentFunction=9'],
# 	['CVL07209R', 'SectorEquipmentFunction=7'],
# 	['CVL07209R', 'SectorEquipmentFunction=8'],
# 	['CVL07209R', 'SectorEquipmentFunction=9'],
# 	['CVL07209R', 'SectorEquipmentFunction=13'],
# 	['CVL07209R', 'SectorEquipmentFunction=14'],
# 	['CVL07209R', 'SectorEquipmentFunction=15'],
# 	['CVL07209R', 'SectorEquipmentFunction=16'],
# 	['CVL07209R', 'SectorEquipmentFunction=17'],
# 	['CVL07209R', 'SectorEquipmentFunction=18'],
# 	['CVL07209R', 'SectorEquipmentFunction=19'],
# 	['CVL07209R', 'SectorEquipmentFunction=20'],
# 	['CVL07209R', 'SectorEquipmentFunction=21]']
# ]
# eq_list = [item for item in elist if item[0] == 'CVL07209R']
# mos = [item for item in eq_list if eq_list.count(item) > 1]
# print(mos)
# print(len(mos))
adict = {
	'CVL01207_7A_1': 'B17',
	'CVL01207_7B_1': 'B17',
	'CVL01207_7C_1': 'B17',
	'CVL01207_9A_1': 'B2',
	'CVL01207_9B_1': 'B2',
	'CVL01207_9C_1': 'B2',
	'CVL01207_3A_1': 'B30',
	'CVL01207_3B_1': 'B30',
	'CVL01207_3C_1': 'B30',
	'CVL07209_2A_1': 'B4',
	'CVL07209_2B_1': 'B4',
	'CVL07209_2C_1': 'B4',
	'CVL07209_2A_3': 'B66',
	'CVL07209_2B_3': 'B66',
	'CVL07209_2C_3': 'B66',
	'CVL07209_8A_1': 'B5',
	'CVL07209_8B_1': 'B5',
	'CVL07209_8C_1': 'B5',
	'CVL07209_7A_2_E': 'B29',
	'CVL07209_7B_2_E': 'B29',
	'CVL07209_7C_2_E': 'B29',
	'CVL07209_7A_3_F': 'B14',
	'CVL07209_7B_3_F': 'B14',
	'CVL07209_7C_3_F': 'B14'
}
dlonly = ['B17', 'B12']
item = set(dlonly).issubset(adict.values())
print(item)
