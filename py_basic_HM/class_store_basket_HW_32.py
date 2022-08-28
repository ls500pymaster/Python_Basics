class Item:

	def __init__(self, name, price, decription, dimensions):
		self.price = price
		self.decription = decription
		self.dimensions = dimensions
		self.name = name

	def __str__(self):
		return f"Item = {self.name}, Price = {self.price}, Spec = {self.decription}, Size = {self.dimensions}"


class User:

	def __init__(self, name, surname, numberphone):
		self.name = name
		self.surname = surname
		self.numberphone = numberphone

	def __str__(self):
		return f"Name: {self.name} \n Surname: {self.surname} \n Phone: {self.numberphone}\n"


class Purchase:
	def __init__(self, user):
		self.products = {}
		self.user = user
		self.total = 0

	def add_item(self, item, cnt):
		self.products[item] = cnt

	def __str__(self):
		return f"Customer: \n {self.user} \n Count: {self.products} \n {self.total}"

	def get_total(self):
		return self.products.keys(), self.products.values()


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
# print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 2)
cart.add_item(apple, 3)

print(cart.get_total())
