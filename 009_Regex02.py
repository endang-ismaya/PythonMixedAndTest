import re
"""
regex sub function
"""

phone = "Please call the phone # +61-927 479-548"

# remove anything other than digits
num = re.sub(r'\D', "", phone)
print("The raw phone number is: " + num)

"""
regex split
"""
print("-" * 50)
line = "Learn, Scientific, Python"
line2 = "+61learn7489Scientific324234"

m = re.split('\W+', line)
m1 = re.split(r'[A-Za-z]+', line2, re.I)

if m:
	print(m)
else:
	print("No Match!")
print("-" * 50)
if m1:
	print(m1)
else:
	print('No match!')

"""
regex findall
"""
print("-" * 50)
line = "your alpha_1@scientificprogramming.io, blah beta@scientificprogramming.io blah user"

emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)

if emails:
	print(emails)
else:
	print("No match!")

print("-" * 50)
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', line)
if tuples:
	print(tuples)
	print(tuples[0])
else:
	print('No match!')
