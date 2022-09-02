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

	def get_total(self):
		new = []
		new2 = []
		self.count = 0
		self.total_item = 0
		for value in self.products.values():
			new.append(value)
		for key in self.products.keys():
			new2.append(key.price)
		tb = [a * b for a, b in zip(new, new2)]
		for item in tb:
			self.count += item
		return self.count

	def cart_info(self):
		tmp = ""
		for k, v in self.products.items():
			tmp += f"{k.name} --> {v} pcs.\n"
		return tmp

	def __str__(self):
		return f"Customer\n{self.user}\nItems: \n{self.cart_info()}"

lemon = Item('Lemon', 5, "yellow", "small", )
apple = Item('Apple', 5, "red", "medium", )
rukola = Item('Rukola', 20, "green", "large")
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(lemon, 3)
cart.add_item(apple, 2)
cart.add_item(rukola, 1)
print(cart)
full_cart = cart.get_total()
print(full_cart)
