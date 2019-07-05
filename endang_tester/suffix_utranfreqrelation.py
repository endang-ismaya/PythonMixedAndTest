"""
Suffix UtranFreqRelation v1.0.0
Created: 4/12/2018
Update: -
"""

class FindBaseline:

	def __init__(self, final_srtdb, eutrancellfdd, utranfreq):
		self._final_srtdb = final_srtdb
		self._eutrancellfdd = eutrancellfdd
		self._utranfreq = utranfreq
		self.__baseline = ''

	def get_baseline(self):
		return self.__baseline

