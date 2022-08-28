class Basket:
	def __init__(self, name, price, spec, dimension):
		self._name = name
		self._price = price
		self._spec = spec
		self._dimension = dimension

	def __str__(self):
		return f"name = {self._name}, price = {self._price}, spec = {self._spec}, dimension = {self._dimension}"


class Customer:
	def __init__(self, name, surname, phone, userid):
		self._name = name
		self._surname = surname
		self._phone = phone
		self._userid = userid

	def __str__(self):
		return f"Name: {self._name} \n Surname: {self._surname} \n Phone: {self._phone}\n"


class Order:
	def __init__(self, customer):
		self._products = {}
		self._customer = customer

	def add_item(self, item, count):
		count = 0
		self._products[item] = count

	def __str__(self):
		return f"customer = {self._customer}"

	def get_total(self):
		return f"Customer: \n {self._customer} \n Count: {self._products} \n {self._products.values()} \n {self._products.items()}\n"


lemon = Basket("lemon", 5, "yellow", "small", )
apple = Basket("apple", 10, "green", "medium")
buyer = Customer("Alexander", "Python", "048100500", "0")
cart = Order(buyer)
cart.add_item(lemon, 2)
cart.add_item(apple, 3)

print(cart.get_total())
