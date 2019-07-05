"""
srt check reader test
"""
import os
import sqlite3

path = r'C:\cygwin\home\endang.ismaya\ts_esrtlog\GeSRT\FirstNet_IDLe'
db_path = os.path.join(path, '20180403_080502_CVL01207_CVL07209R_srtdb.db')

# cr_invxr = SrtCheckReader(path, 3)
# cr_invxr.create_invxr()
# print('\n')
# print('Invxr profile save as: ' + cr_invxr.get_csv_filename)
# print('Sqlite db save as : ' + cr_invxr.get_sqliltedb_naming)


db_conn = sqlite3.connect(db_path)
cur = db_conn.cursor()

fdd = "EUtranCellFDD"
param = "acBarringForCsfb.acBarringFactor"

cur.execute(
	"select * from Parsed where moclass=? and parameter=?",
	(fdd, param)
)

rows = cur.fetchall()

for row in rows:
	print(row)

cur.execute(
	"select siteid,fga_selection from SiteProfile"
)

rows = cur.fetchall()
for row in rows:
	print(row)

db_conn.close()
