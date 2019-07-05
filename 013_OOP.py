"""
Mahmoud Ahmed
"""

def cr_line():
	print("-" * 50)
	print()

# --------------
# OOP example 1
# --------------
cr_line()
class MyClass(object):
	class_value = 'value of the class'


d = MyClass()
print(d.class_value)

d.class_value = 'Endang.Ismaya'
print(d.class_value)

del d.class_value
print(d.class_value)

# --------------
# OOP example 2
# --------------
cr_line()
class Student:
	def __init__(self, name):
		self.name = name
		self.marks = []  # this is list
		print("Welcome to the school, {}!".format(name))

	def addmarks(self, mark):
		self.marks.append((mark))

	def avg(self):
		return sum(self.marks)/len(self.marks)


a = Student('Endang')
a.addmarks(50)
a.addmarks(100)
a.addmarks(90)
a.addmarks(80)
print(a.avg())

# --------------
# OOP example 3
# --------------
cr_line()
class Calculator:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b

	def multiple(self):
		return self.a + self.b


calc = Calculator(20, 50)
print(calc.add())
print(calc.multiple())

cr_line()
