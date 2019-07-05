class Animal:
	noise = "Grunt"
	size = "large"
	color = "Brown"
	hair = "Covers body"

	def get_color(self):
		return self.color

	def make_noise(self):
		return self.noise

class Dog(Animal):
	name = 'Jon'


obj = Dog()
mycolor = obj.get_color()
print(mycolor)
