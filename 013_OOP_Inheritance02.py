"""
Mahmoud Ahmed
"""

class Animal:
	def __init__(self, name):
		self.name = name


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.food = 'fish'

	def fetch(self, thing):
		print('%s goes after the %s' %(self.name, thing))


d = Dog('Misho')
print(d.name)
print(d.food)


# Multiple inheritance
class A:
	def dothis(self):
		print('Doing this in A')

class B(A):
	pass

class C:
	def dothis(self):
		print('Doing this in C')

class D(B, C):
	# pass
	print('Doing this in D')


d = D()
d.dothis()
print(D.mro())
