"""
Bill Weinman
"""

def main():
	print('This is the 015_Yield.py file')
	for i in inclusive_range(0, 25, 1):
		print(i, end=' ')
	print()
	for i in inclusive_range_pro(20):
		print(i, end=' ')
	print()
	for i in inclusive_range_pro(23, 25):
		print(i, end=' ')
	print()
	for i in inclusive_range_pro(0, 20, 2):
		print(i, end=' ')

def inclusive_range(start, stop, step):
	i = start
	while i <= stop:
		yield i
		i += step

def inclusive_range_pro(*args):
	num_args = len(args)
	if num_args < 1:
		raise TypeError('requires at least one argument')
	elif num_args == 1:
		start = 0
		stop = args[0]
		step = 1
	elif num_args == 2:
		(start, stop) = args
		step = 1
	elif num_args == 3:
		(start, stop, step) = args
	else:
		raise TypeError('inclusive_range_pro expected at most 3 arguments, got ()'.format(args))
	i = start
	while i <= stop:
		yield i
		i += step

if __name__ == '__main__':
	main()

