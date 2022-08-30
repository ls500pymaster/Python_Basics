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

	def get_total_cart(self):
		for key, value in self.products.items():
			print(key, value)

	def get_total_bill(self):
		self.total_bill = 0
		self.total_item = 0
		for k, v in self.products.items():
			self.total_item += v
			self.total_bill += k.price
		return f"\nTotal items: {self.total_item}\nTotal bill: {self.total_bill}"


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "medium", )
rukola = Item('rukola', 20, "green", "large")
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(apple, 2)
cart.add_item(lemon, 1)
cart.add_item(rukola, 1)
print(buyer)
full_cart = cart.get_total_cart()
full_cart
print(cart.get_total_bill())
