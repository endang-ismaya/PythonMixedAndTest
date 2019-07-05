"""
SRT Check dbCreate v1.0.0
Created: 4/2/2018
Update: -
"""
import sqlite3
import os

class CreateSRTCheckDb:

	__db_fullpath = ''

	def __init__(self, srtcheck_datas, path_filename):
		self._srtcheck_datas = srtcheck_datas
		self.__db_fullpath = path_filename

	def create_db(self):
		# db_file = 'siteid_srtdb.db'
		# self.__db_fullpath = os.path.join(self._path_folder, db_file)
		if os.path.exists(self.__db_fullpath):
			os.remove(self.__db_fullpath)

		db_conn = sqlite3.connect(self.__db_fullpath)
		print("Database's created.")

		# the_cursor = db_conn.cursor()
		db_conn.execute("DROP TABLE IF EXISTS Invxr")
		db_conn.commit()

		try:
			db_conn.execute("""
				CREATE TABLE Invxr(
				siteid TEXT, eutrancellfdd TEXT, fru TEXT, rf TEXT,
				lnh TEXT, board TEXT, branch TEXT, dlattenuation TEXT, dltrafficdelay TEXT,
				ulattenuation TEXT, ultrafficdelay TEXT);
			""")

			db_conn.commit()
		except sqlite3.OperationalError as err:
			print("Table Invxr couldn't be created: ", err)

		print("Table Invxr created.")
		db_conn.close()
		# print("Database closed.")

	def insert_db(self):
		db_conn = sqlite3.connect(self.__db_fullpath)

		for data in self._srtcheck_datas:
			# print(data)
			db_conn.execute(
				'insert into Invxr values (?,?,?,?,?,?,?,?,?,?,?)', data
			)
			db_conn.commit()
		print('Table has been inserted.')
		db_conn.close()
		print("Database closed.")

	def print_db(self):
		# pass
		db_conn = sqlite3.connect(self.__db_fullpath)
		the_cursor = db_conn.cursor()

		try:
			result = the_cursor.execute(
				"SELECT * FROM Invxr WHERE eutrancellfdd=" + "'" + "CVL01207_7A_1" + "'"
			)
			for row in result:
				print(row)
		except sqlite3.OperationalError as err:
			print("The table doesn\'t exist!", err)

		db_conn.close()
		print('DB closed at print_db')
