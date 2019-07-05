import re

"""
regex lookahead
"""
# line = "begin:learner1:scientific:learner2:scientific:learner3:end"
# print(re.findall(r'(\w+)(?=:scientific)', line))
# print(re.findall(r'(learner\d+)(?!:scientific)', line))
#
# print("-" * 50)
# line = "Learn scientific programming"
# line1 = "Learn programming"
# pattern = r'(scientific )?programming'
# regex = re.compile(pattern)
# m1 = regex.search(line1)
# m2 = regex.search(line)
#
# print(m1.group())
# print(m2.group())


line1 = [
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,EUtranFreqRelation=2175,EUtranCellRelation=310410-671206-24',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,EUtranFreqRelation=2175,EUtranCellRelation=CVL07209_2A_1',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,EUtranFreqRelation=825,EUtranCellRelation=310410-670688-10',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,EUtranFreqRelation=2456',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,UtranFreqRelation=4360,UtranCellRelation=310410-75-6598',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3A_1,UtranFreqRelation=4360,UtranCellRelation=CNU5678A',
	'ENodeBFunction=1,EUtranCellFDD=CVL01207_3B_1,UtranFreqRelation=512']

for line in line1:
	print(re.findall(r'.*,EUtranCellFDD=(\w+),?.*Relation=([\w-]+)', line))
