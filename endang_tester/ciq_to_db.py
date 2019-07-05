"""
NCAL CIQ to DB v1.0.0
Created: 4/9/2018
Update: -
"""
import sqlite3
import os
import csv

from endang_tester import ciq_relations_db_class

class CiqToDb:

	def __init__(self, final_srtdb, ciq_folder):
		self._final_srtdb = final_srtdb
		self._ciq_folder = ciq_folder
		# self._ciq_pci_ncal = os.path.join(self._ciq_folder, 'CIQ_PCI_NCAL.txt')
		# self._ciq_enbinfo_ncal = os.path.join(self._ciq_folder, 'CIQ_ENBINFO_NCAL.txt')
		# self._ciq_eutranparams_ncal = os.path.join(self._ciq_folder, 'CIQ_EUTRANPARAMETER_NCAL.txt')
		self._ciq_lteumts_ncal = os.path.join(self._ciq_folder, 'CIQ_LTEUMTS_NCAL.txt')
		self._ciq_ltelte_ncal = os.path.join(self._ciq_folder, 'CIQ_LTELTE_NCAL.txt')
		self.__dict_fdd_siteid = {}
		self.__relations_datas = []

	@property
	def get_dict_fdd_siteid(self):
		return self.__dict_fdd_siteid

	@property
	def get_relations_datas(self):
		return self.__relations_datas

	def __create_dict_fdd_siteid(self):
		db_conn = sqlite3.connect(self._final_srtdb)
		cur = db_conn.cursor()
		cur.execute("""select distinct siteid,currentvalue from Parsed 
		where moclass='sectorcarrier' collate nocase
		and parameter='reservedBy.reservedBy' collate nocase
		and currentvalue like '%EUtranCellFDD%'
		""")
		rows = cur.fetchall()
		for row in rows:
			# print(str(row[0]), str(row[1]).split('=')[-1])
			siteid = str(row[0])
			fdd = str(row[1]).split('=')[-1]
			self.__dict_fdd_siteid[fdd] = siteid

	def __set_relation_data(self):
		with open(self._ciq_ltelte_ncal) as f:
			reader = csv.DictReader(f, delimiter='#', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
			for row in reader:
				if row['EUtranCellFDD'] in self.get_dict_fdd_siteid.keys():
					self.__relations_datas.append(
						[str(row['EUtranCellFDD']), str(row['EutranFreqRelationID']), '--county--', 'EUtranFreqRelation']
					)

		with open(self._ciq_lteumts_ncal) as f:
			reader = csv.DictReader(f, delimiter='#', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
			for row in reader:
				if row['EUtranCellFDD'] in self.get_dict_fdd_siteid.keys():
					self.__relations_datas.append(
						[str(row['EUtranCellFDD']), str(row['UtranFreqRelationId']), str(row['County']), 'UtranFreqRelation']
					)

	def set_relation_data_to_db(self):
		self.__create_dict_fdd_siteid()
		self.__set_relation_data()

		ciq_rel = ciq_relations_db_class.CreateCIQRelationDb(self.get_relations_datas, self._final_srtdb)
		ciq_rel.create_db()
		ciq_rel.insert_db()


def main():
	dbpath = r'D:\Programming\Python\eranris\kguts_pro\Kget_sample\FirstNet_IDLe' \
			r'\20180409_155911_CVL01207_CVL07209R_srtdb_TESTER.db '

	ciqpath = r'D:\Work\Yupana\ATT\SRT.BAU\NCAL_SRT\LTE\CIQ\SFO_LTE_RNDCIQ_REV_362_04032018'

	create_ciq_db = CiqToDb(dbpath, ciqpath)
	create_ciq_db.set_relation_data_to_db()

if __name__ == '__main__':
	main()
