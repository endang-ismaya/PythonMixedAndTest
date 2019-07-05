"""
Tuples:
* A tuple is an immutable list (can't be changed/ modified)
* Tuples are ordered
* Values accessed by index
* Iteration, looping, concatenation
* Use when data should not change
* Tuples can be deleted
"""
"""
Casting Tuples:
* list()    : Built-in function returns a list.
* tuple()   : Built-in function returns a tuple
* type()    : Built-in function returns an object's type
"""

days_of_the_week = (
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
	'Sunday'
)

monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
	print(day)