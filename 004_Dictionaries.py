"""
Dictionaries:
* Hold key-value pairs called items.
* AKA associative arrays, hash tables and hashes
"""

"""
Declaring Dictionary
"""
dictionary_name = {
	"key_1": "value_1",
	"key_2": "value_2",
	"key_3": "value_3",
}
""" Empty Dictionary """
dictionary_name1 = {}

""" Sample """
contacts = {
	'Endang': '0813-87087080',
	'Indah': '0812-95919090'
}

endang_phone = contacts['Endang']
indah_phone = contacts['Indah']

print('Dial {} to call Endang.'.format(endang_phone))
print('Dial {} to call Indah'.format(indah_phone))

# set dictionary's value by key
# -----------------------------
contacts['Endang'] = '0812-95919091'
endang_phone = contacts['Endang']

print()
print('Dial {} to call Endang.'.format(endang_phone))

# Add key and value to Dictionary
# -------------------------------

contacts['Aldeind'] = '0812-95919092'
print()
print(contacts)
print(len(contacts))

# Dictionary with different data type
# -----------------------------------

contacts2 = {
	'Endang': ['0813-87087080', '0812-95919091'],
	'Indah': '0812-95919090'
}

print()
print('Endang:')
print(contacts2['Endang'])
print(contacts2['Endang'][0])
print('Indah')
print(contacts2['Indah'])

# Looping through Dictionary
# --------------------------
print()
for number in contacts2['Endang']:
	print('Phone: {}'.format(number))

# Check if keys exist in dictionary
# ----------------------------------
print()
if 'Endang' in contacts2.keys():
	print("Endang's phone number is: ")
	print(contacts2['Endang'])

if 'Aldeind' in contacts2.keys():
	print("Aldeind's phone number is: ")
	print(contacts2['Aldeind'])
else:
	print('Aldeind is not in the contact2 list')

# Check if value exist in dictionary
# ----------------------------------
print()
print('0813-870870870' in contacts2.values())
