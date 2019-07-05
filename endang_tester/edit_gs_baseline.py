import sqlite3
from endang_tester import stopwatch

sw = stopwatch.Timer()
print(sw.start())
print('-' * 50)
print()

idl2_db = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\9625_DUS_IDL2\20180420_225157_CVL02267_srtdb.db'
baseband = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe' \
           r'\20180420_222532_CVL01207_CVL07209R_srtdb.db'
baseline = r'D:\Programming\Python\eranris\kguts_pro\gs_baseline\gesrt_baseline.db'

db_conn = sqlite3.connect(baseline)
cur = db_conn.cursor()

# cur.execute("""select sql from sqlite_master where type = 'table' and name = 'GSRev_17_38'""")
# print(cur.fetchall())

cur.execute("""
select * from GSRev_17_38 where moc='AirIfLoadProfile' and parameter='ocngPrbSerie.prbLast' collate nocase
""")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("""
update GSRev_17_38
set gs_baseline='0'
where moc='AirIfLoadProfile' and parameter='ocngPrbSerie.prbLast' collate nocase
""")
db_conn.commit()

cur.execute("""
select * from GSRev_17_38 where moc='AirIfLoadProfile' and parameter='ocngPrbSerie.prbLast' collate nocase
""")
rows = cur.fetchall()
for row in rows:
    print(row)

print(sw.stop())
print('-' * 50)
print()

db_conn.close()

# GSRev_17_38
# cur.execute("""select name from sqlite_master where type = 'table'""")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
