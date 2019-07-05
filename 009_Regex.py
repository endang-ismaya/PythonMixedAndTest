import re

line = "Learn to Analyze Data with Scientific Python"
m = re.match(r'(.*) to (.*?) .*', line, re.M | re.I)
if m:
	print("m.group(): ", m.group())
	print("m.group(1): ", m.group(1))
	print("m.group(2): ", m.group(2))
else:
	print("No Match!!")


"""
Match and Search
"""
print("-" * 125)
email = "hello@leremove_thisarntoanalyzedata.com"

m = re.search("remove_this", email)

if m:
	print("email address: ", email[:m.start()] + email[m.end():])
else:
	print("No Match!!")

print("-" * 125)
#
m = re.search(r'(python)', line, re.M | re.I)
if m:
	print("m.group(): ", m.group())
else:
	print("No match by obj.search!!")

print("-" * 125)
m = re.match(r'python', line, re.M|re.I)
if m:
	print("m.group: ", m.group())
else:
	print("No match by obj.match")


"""
regex group
"""
print("-" * 125)
name = "Learn Scientific"

m = re.match("(?P<first>\w+)\W+(?P<last>\w+)", name)
if m:
	print(m.group('first'))
	print(m.group('last'))

"""
groupdic() method
"""
print("-" * 125)
name = "Scientific Python"

# Match names
m = re.match("(?P<first>\w+)\W+(?P<last>\w+)", name)

if m:
	# Get dict
	d = m.groupdict()
	# Loop over dictionary with for-loop
	for t in d:
		print("key  : ", t)
		print("value: ", d[t])

