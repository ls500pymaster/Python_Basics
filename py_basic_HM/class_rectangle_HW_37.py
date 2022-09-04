class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def get_square(self):
		return self.width * self.height

	def __eq__(self, other):
		return self.get_square()==other.get_square()

	def __add__(self, other):
		return Rectangle(1, self.get_square() + other.get_square())

	def __mul__(self, n):
		return Rectangle(self.width, n * self.height)

	def __str__(self):
		return f"Rectangle w: {self.width}, h: {self.height}, s: {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())  # 8
print(r2.get_square())  # 18

r3 = r1 + r2
print(r3.get_square())  # 26

r4 = r1 * 4
print(r4.get_square())  # 32
