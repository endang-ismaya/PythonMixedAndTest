"""
Parsed dbCreate v1.0.0
Created: 4/3/2018
Update: -
"""

import sqlite3

class CreateParsedDb:

	def __init__(self, parsed_data, path_filename):
		self._parsed_datas = parsed_data
		self._db_fullpath = path_filename

	def create_db(self):
		# if os.path.exists(self.__db_fullpath):
		# 	os.remove(self.__db_fullpath)

		db_conn = sqlite3.connect(self._db_fullpath)
		print("->CreateParsedDb using database: " + self._db_fullpath)

		# the_cursor = db_conn.cursor()
		# db_conn.execute("DROP TABLE IF EXISTS Invxr")
		# db_conn.commit()

		try:
			db_conn.execute("""
				CREATE TABLE if not exists Parsed(
				siteid TEXT, mo TEXT, moclass TEXT, parameter TEXT,
				currentvalue TEXT, source_element TEXT, target_element TEXT
				);
			""")

			db_conn.commit()
			print("->Table Parsed created.")
		except sqlite3.OperationalError as err:
			print("->Table Parsed couldn't be created: ", err)

		db_conn.close()
		print("->Database closed @CreateParsedDb.create_db")

	def data_generator(self):
		for data in self._parsed_datas:
			yield data

	def insert_db(self):
		db_conn = sqlite3.connect(self._db_fullpath)
		cur = db_conn.cursor()
		print("->Populating table 'Parsed'....")
		# for data in self._parsed_datas:
		# print(data)
		cur.executemany(
			'insert into Parsed values (?,?,?,?,?,?,?)', self.data_generator()
		)

		db_conn.commit()
		print('->Table Parsed has been populated.')
		db_conn.close()
		print("->Database closed @CreateParsedDb.insert_db")
