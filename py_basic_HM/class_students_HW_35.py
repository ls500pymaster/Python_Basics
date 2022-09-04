class MyCustomError(Exception):
	def __init__(self, message):
		super().__init__()
		self.message = message

	def get_exception_message(self):
		return self.message

class Human:

	def __init__(self, gender, age, first_name, last_name):
		self.gender = gender
		self.age = age
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return f"Gender: {self.gender} \n Age: {self.age} \n {self.first_name} \n {self.last_name}"


class Student(Human):

	def __init__(self, gender, age, first_name, last_name, record_book):
		self.gender = gender
		self.age = age
		self.first_name = first_name
		self.last_name = last_name
		self.record_book = record_book

	def __str__(self):
		return f"\nName: {self.first_name}\nLast: {self.last_name}\nGender: {self.gender}\nAge: {self.age}"


class Group:
	def __init__(self, number):
		self.number = number
		self.group = set()

	def add_student(self, student):
		if len(self.group) >= 4:
			raise MyCustomError("More than 4")
		try:
			self.group.add(student)
		except MyCustomError as err:
			return (err.get_exception_message())

	def delete_student(self, last_name):
		res = self.find_student(last_name)
		if res==last_name:
			self.group.discard(last_name)
		return None

	def find_student(self, last_name):
		for param in self.group:
			if last_name==param.last_name:
				return param.last_name
			return None

	def __str__(self):
		all_students = set()
		for self.student in self.group:
			all_students.add(self.student)
		return f'{self.student}\n'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Male', 29, 'Ilon', 'Mask', 'AN143')
st3 = Student('Male', 30, 'Baiden', 'Jobs', 'AN142')
st4 = Student('Male', 29, 'Trump', 'Mask', 'AN143')
st5 = Student('Male', 30, 'Obama', 'Jobs', 'AN142')
gr = Group('Group Number 1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
print(gr.find_student("Jobs"))
print(gr.find_student("Test"))  # None
print(gr)  # Student
# gr.delete_student('Jobs')
