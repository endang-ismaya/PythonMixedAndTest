"""
Bill Weinman
"""
import sys
import os
# import urllib.request
import random
import datetime

def main():
	print('Pyhton version {}.{}.{}'.format(*sys.version_info))
	print(sys.platform)

	print(os.name)
	print(os.getenv('PATH'))
	print(os.getcwd())
	print(os.urandom(25))

	# page = urllib.request.urlopen('http://eranris.com/')
	# for line in page:
	# 	print(str(line, encoding='utf_8'), end='')

	print(random.randint(1, 10))
	x = list(range(25))
	print(x)
	random.shuffle(x)
	print(x)

	now = datetime.datetime.now()
	print(now)
	print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__':
	main()
