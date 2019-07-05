"""
Bill Weinman
"""

def lines():
	print()
	print('-' * 130)
	print()

# Declaration
d = {'one': 1, 'two': 2, 'three': 3}
print(d)
e = dict(one=1, two=2, three=3)
print(e)
print(type(d))
x = dict(four=4, five=5, six=6)
print(x)

# combine dict
f = dict(**e, **x, seven=7, eight=8, nine=9, ten=10)
print(f)

lines()
# find key in dict
if 'one' in f:
	print('Yes')
else:
	print('No')
# loop through key
for k in f:
	print(k)
lines()
# loop through key and value
for k, v in f.items():
	print(k, v)
lines()
# get value from key
print(f.get('ten', '_NA_'))
print(f.get('eleven', '_NA_'))
lines()
# delete record
del f['ten']
print(f)
# shown and delete
print(f.pop('seven'))
print(f)

