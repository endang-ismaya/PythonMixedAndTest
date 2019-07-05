def CoverageRelation(SourceCell, TargetCell):
	print('// Source UtranCell  : ' + SourceCell)
	print('// Target UtranCell  : ' + TargetCell)
	print('cr RncFunction=1,UtranCell=' + SourceCell+',CoverageRelation='+ TargetCell)
	print('UtranCell='+ TargetCell+' #utranCellRef')
	print('lset RncFunction=1,UtranCell=' + SourceCell+',CoverageRelation='+ TargetCell+'$ coverageIndicator 1')
	print('lset RncFunction=1,UtranCell=' + SourceCell+',CoverageRelation='+ TargetCell+'$ relationCapability '
			'dchLoadSharing=0,hsCellSelection=0,hsLoadSharing=1')


# SourceCell = input('Source UtranCell: ')
# TargetCell = input('Target UtranCell: ')
# CoverageRelation(SourceCell, TargetCell)

SourceCell = ''
TargetCell = ''

while SourceCell != 'quit' or TargetCell != 'quit':
	SourceCell = input("Source: \n")
	if SourceCell != 'quit':
		TargetCell = input("Target: \n")
		if TargetCell != 'quit':
			CoverageRelation(SourceCell, TargetCell)
		else:
			break
	else:
		break
