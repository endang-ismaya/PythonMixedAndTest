import os
import re
import sqlite3
from collections import Counter
from endang_tester import stopwatch

baseband = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe' \
           r'\20180420_222532_CVL01207_CVL07209R_srtdb.db'

dus = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\DUSQ3_CVL02290_CVL02488_CVL09078R' \
      r'\20180419_061416_CVL02290_CVL02488_CVL09078R_srtdb.db'

wll = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\WLL_CCL08098L\20180425_050039_CCL08098L_srtdb.db'

gs_baseline_db = r'D:\Programming\Python\eranris\kguts_pro\gs_baseline' \
                 r'\gesrt_baseline.db'

sw = stopwatch.Timer()
print(sw.start())
print('-' * 50)
print()

db_conn = sqlite3.connect(gs_baseline_db)
cur = db_conn.cursor()

# list_parser = ()
cur.execute("""
select * from GSRev_17_38 where sw='L17Q3G2'
and moc like 'FeatureState=CXC4010319'
""")
rows = cur.fetchall()
parsed_list = tuple(rows)
# seen = set()
# siteid = item[0]
# mo = item[1]
# moclass = item[2]
# parameter = item[3]
# current_value = item[4]
# source_element = item[5]
# target_element = item[6]
for plist in parsed_list:
    print(plist)


db_conn.close()

print(sw.stop())
print('-' * 50)
print()

# ('CVL02267', 'ENodeBFunction=1,AirIfLoadProfile=PILOT_S1', 'AirIfLoadProfile', 'ocngPrbSerie[0].pdschModType',
#  '0', 'AirIfLoadProfile=PILOT_S1', '')

# r_fdds = set(e[5] for e in fdds)
# print(len(list_parser))
# rows = [item for item in list_parser if item[2] == 'AdmissionControl' and item[3] == 'admNrRbDifferentiationThr']
# for row in rows:
# 	print(row)

# cur.execute("""select name from sqlite_master where type = 'table'""")
# rows = cur.fetchall()
# for row in rows:
# 	print(row)
#
# cur.execute("""select sql from sqlite_master where type = 'table' and name = 'FCNProfile'""")
# print(cur.fetchall())

# ('Invxr',)
# ('Parsed',)
# ('Ncal_ciq_relations',)
# ('SiteProfile',)
# ('CellProfile',)
# ('Relation_fcn_alias',)
# ('FCNProfile',)
# ('sqlite_sequence',)
# ('Missing_UtranFreqRelation',)
# ('Missing_EUtranFreqRelation',)
# ('Missing_ColocatedLteLte',)
