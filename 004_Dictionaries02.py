"""
Loops through dictionary
"""

# Nest dictionary
# ---------------
contacts = {
	'Endang': {
		'phone': ['0813-87087080', '0812-95919091'],
		'email': 'endang.ismaya@eranris.com'
	},
	'Indah': {
		'phone': '0812-95919090',
		'email': 'indahdwi.anggraeny@eranris.com'
	}
}

for contact in contacts:
	print("{}'s contact info: ".format(contact))
	print(contacts[contact]['phone'])
	print(contacts[contact]['email'])

