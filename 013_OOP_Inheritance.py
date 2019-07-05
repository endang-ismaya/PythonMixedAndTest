"""
Mahmoud Ahmed
"""

def cr_line():
	print("-" * 50)
	print()

class Calculator:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def sum(self):
		return self.x + self.y

	def multiple(self):
		return self.x * self.y


class Scientific(Calculator):
	def power(self):
		return pow(self.x, self.y)

calc = Calculator(10, 2)
print(calc.sum())
print(calc.multiple())

cr_line()

sc = Scientific(10, 2)
print(sc.sum())
print(sc.multiple())
print(sc.power())
print(10**2)
