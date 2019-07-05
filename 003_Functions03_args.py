"""
Bill Weinman
"""

# args
# def main():
# 	test_func(1, 2, 3, 42, 43, 45, 46)
#
# def test_func(this, that, other, *args):
# 	print(this, that, other)
# 	for n in args:
# 		print(n, end=':')


# kwargs
def main():
	test_func(5, 6, 7, 8, 9, 10, one=1, two=2, three=33)


def test_func(this, that, other, *args, **kwargs):
	print(this, that, other)
	for n in args:
		print(n)
	for k in kwargs:
		print(k, ":", kwargs[k])


if __name__ == "__main__":
	main()
