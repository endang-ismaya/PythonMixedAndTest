"""
Bill weinman
Conditionals
"""

a, b = 5, 1
if a < b:
	print('a ({}) is less than b ({}))'.format(a, b))
else:
	print('a ({}) is not less than b ({})'.format(a, b))

# sugar syntax
print("foo" if a < b else "bar")
