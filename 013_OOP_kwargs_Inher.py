"""
Bill Weinman
"""

class Animal:
	def talk(self):
		print('I have something to say!')

	def walk(self):
		print('Hey!, I''m walking'' here!')

	def clothes(self):
		print('I have nice clothes')

# ------------------------
# Flexibility object date
# ------------------------
class Duck(Animal):
	def __init__(self, **kwargs):
		self.variables = kwargs

	def quack(self):
		print('Quaaaakk!')

	def walk(self):
		super().walk()
		print('Walk like a duck.')

	def set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)

class Dog(Animal):
	def clothes(self):
		print('I have brown and white fur')

def main():
	donald = Duck()
	donald.quack()
	donald.walk()
	donald.clothes()

	dog = Dog()
	dog.clothes()
	dog.talk()


if __name__ == '__main__':
	main()

