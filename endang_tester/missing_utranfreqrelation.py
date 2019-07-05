"""

"""

missing_utran = """
CVL07209_2A_1->487, CVL07209_2A_1->512, CVL07209_2B_1->487, CVL07209_2B_1->512,
CVL07209_2C_1->487, CVL07209_2C_1->512, CVL07209_7A_3_F->487, CVL07209_7A_3_F->512,
CVL07209_7B_3_F->487, CVL07209_7B_3_F->512, CVL07209_7C_3_F->487, CVL07209_7C_3_F->512,
CVL07209_8A_1->487, CVL07209_8A_1->512, CVL07209_8B_1->487, CVL07209_8B_1->512,
CVL07209_8C_1->487, CVL07209_8C_1->512,  
"""

class CreateMissingUtranFreq:

	def __init__(self, target_list, final_srtdb):
		self._target_list = target_list
		self._final_srtdb = final_srtdb

	
