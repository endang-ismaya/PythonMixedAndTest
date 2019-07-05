"""
John Harper
4/14/2018
"""

# Map
# def mapping(x):
# 	return x*100
#
# inputs = [1, 5, 3, 2, 5, 5, 45, 6]
#
# new_list = list(map(mapping, inputs))
# print(new_list)
#
# # Filter
# number_list = [10, 4, 20.5, 200, 70, 32.2, 70, 45, 88, 45, 900]
# less_than_zero = list(filter(lambda x: x % 10 == 0, number_list))
# print(less_than_zero)


def mapping2(x):
	y = x[0] * 10
	z = x[1] * 15
	return y, z

inputs = [
	[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]
]

print(map(mapping2(inputs)))

