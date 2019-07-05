"""
CIQ EUtranFreq and UtranFreq to db v1.0.0
Created: 4/9/2018
Update: -
"""

import sqlite3

class CreateCIQRelationDb:

	def __init__(self, parsed_data, path_filename):
		self._parsed_datas = parsed_data
		self._db_fullpath = path_filename

	def create_db(self):
		db_conn = sqlite3.connect(self._db_fullpath)
		print("->CreateNCAL_CIQ_RelationDb using database: " + self._db_fullpath)

		try:
			db_conn.execute("""
				CREATE TABLE if not exists ciq_NCAL_relations(
				eutrancellfdd TEXT, fcn TEXT, county TEXT, type TEXT
				);
			""")

			db_conn.commit()
			print("->Table ciq_NCAL_relations created.")
		except sqlite3.OperationalError as err:
			print("->Table ciq_NCAL_relations couldn't be created: ", err)

		db_conn.close()
		print("->Database closed @CreateCIQRelationDb.create_db")

	def data_generator(self):
		for data in self._parsed_datas:
			yield data

	def insert_db(self):
		db_conn = sqlite3.connect(self._db_fullpath)
		cur = db_conn.cursor()
		print("->Populating table 'ciq_NCAL_relations'....")
		# for data in self._parsed_datas:
		# print(data)
		cur.executemany(
			'insert into ciq_NCAL_relations values (?,?,?,?)', self.data_generator()
		)

		db_conn.commit()
		print('->Table ciq_NCAL_relations has been populated.')
		db_conn.close()
		print("->Database closed @CreateCIQRelationDb.insert_db")
