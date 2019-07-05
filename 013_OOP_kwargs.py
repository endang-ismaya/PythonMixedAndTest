"""
Bill Weinman
"""

# ------------------------
# Flexibility object date
# ------------------------
class Duck:
	def __init__(self, **kwargs):
		self.variables = kwargs

	def quack(self):
		print('Quaaaakk!')

	def walk(self):
		print('Walk like a duck.')

	def set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)


def main():
	donald = Duck(feet=2)
	print(donald.get_variable('feet'))

if __name__ == '__main__':
	main()

