"""
Bill weinman
Loops
"""

# simple fibonacci series
# the sum of two elements defines the next set
# a, b = 0, 1
# while b < 50:
# 	print(b)
# 	a, b = b, a + b

# read the lines from a file
fh = open('D:\\Work\\Yupana\\ATT\\SRT.BAU\\NCAL_SRT\\LTE\\CIQ\\SFO_LTE_RNDCIQ_REV_358_02202018\\CIQ_ENBINFO_NCAL.txt')
for line in fh.read():
	print(line, end='')
