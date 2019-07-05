"""
Missing UtranFreqRelation to db v1.0.0
Created: 4/12/2018
Update: -
"""

import sqlite3

class CreateMissingUtranFreqRelationDb:

	def __init__(self, parsed_data, path_filename):
		self._parsed_datas = parsed_data
		self._db_fullpath = path_filename

	def create_db(self):
		db_conn = sqlite3.connect(self._db_fullpath)
		print("->CreateMissingUtranFreqRelationDb using database: " + self._db_fullpath)

		try:
			db_conn.execute("""
				CREATE TABLE if not exists Missing_UtranFreqRelation(
				sitename TEXT, eutrancellfdd TEXT, utranfreqrelationid TEXT,
				status TEXT, freq_type TEXT, mo TEXT, cellreselectionpriority TEXT,
				allowedplmnlist TEXT, anrmeason TEXT, connectedmodemobilityprio TEXT,
				csfallbackprio TEXT, csfallbackprioec TEXT, lbbnrpolicy TEXT, mobilityaction TEXT,
				mobilityactioncsfb TEXT, pmaxutra TEXT, qoffsetfreq TEXT, qqualmin TEXT, qrxlevmin TEXT,
				threshxhigh TEXT, threshxhighq TEXT, threshxlow TEXT, userlabel TEXT,
				utranfreqtoqciprofilerelation TEXT, voiceprio TEXT, altcsfbtargetprio TEXT,
				altcsfbtargetprioec TEXT, maxnrutrancellrelations TEXT, threshxlowq TEXT
				);
			""")

			db_conn.commit()
			print("->Table Missing_UtranFreqRelation created.")
		except sqlite3.OperationalError as err:
			print("->Table Missing_UtranFreqRelation couldn't be created: ", err)

		db_conn.close()
		print("->Database closed @CreateMissingUtranFreqRelationDb.create_db")

	def data_generator(self):
		for data in self._parsed_datas:
			yield data

	def insert_db(self):
		db_conn = sqlite3.connect(self._db_fullpath)
		cur = db_conn.cursor()
		print("->Populating table 'Missing_UtranFreqRelation'....")
		# for data in self._parsed_datas:
		# print(data)
		cur.executemany(
			'insert into Missing_UtranFreqRelation values ('
			'?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
			')', self.data_generator()
		)

		db_conn.commit()
		print('->Table ciq_NCAL_relations has been populated.')
		db_conn.close()
		print("->Database closed @CreateMissingUtranFreqRelationDb.insert_db")
