class Item:

	def __init__(self, name, price, decription, dimensions):
		self.price = price
		self.decription = decription
		self.dimensions = dimensions
		self.name = name

	def __str__(self):
		return f"Items: {self.name}, Price = {self.price}, Spec = {self.decription}, Size = {self.dimensions} "


class User:

	def __init__(self, name, surname, numberphone):
		self.name = name
		self.surname = surname
		self.numberphone = numberphone

	def __str__(self):
		return f"Name: {self.name}\nSurname: {self.surname}\nPhone: {self.numberphone}\n"


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
		self.total_item = 0
		for k, v in self.products.items():
			self.total_item += v
		new = []
		new2 = []
		self.count = 0
		keys = self.products.keys()
		for value in self.products.values():
			new.append(value)
		for key in self.products.keys():
			new2.append(key.price)
		tb = [a * b for a, b in zip(new, new2)]
		for item in tb:
			self.count += item
		return f"Total items: {self.total_item}\nTotal price of order: {self.count}"  # Total bill: {self.total_bill}"


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 5, "red", "medium", )
rukola = Item('rukola', 20, "green", "large")
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(lemon, 3)
cart.add_item(apple, 2)
cart.add_item(rukola, 1)
print(buyer)
full_cart = cart.get_total()
print(full_cart)
