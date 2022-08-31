class Human:

	def __init__(self, gender, age, first_name, last_name):
		self.gender = gender
		self.age = age
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return f"Gender: {self.gender} \n Age: {self.age} \n {self.first_name} \n {self.last_name}"


class Student(Human):
	def __init__(self, gender, age, first_name, last_name, record_book=1):
		super().__init__(gender, age, first_name, last_name)
		self.gender = gender
		self.age = age
		self.first_name = first_name
		self.last_name = last_name
		self.record_book = record_book

	def __str__(self):
		return f"\nName: {self.first_name}\nGender: {self.gender}\nAge: {self.age}"


class Group(Student):
	def __init__(self, number, student, gender, age, first_name, last_name, record_book=1):
		super().__init__(gender, age, first_name, last_name, record_book)
		self.number = number
		self.student = student
		self.group = set()

	def add_student(self, student: object) -> object:
		self.group.add(student)

	def delete_student(self, last_name):
		res = self.find_student(last_name)
		del res

	def find_student(self, last_name):
		param = input("Input last name: ")
		for last_name in self.student.last_name:
			print(last_name)
			found = True
			if not found:
				print("Error")

	def __str__(self):
		all_students = ''
		...
		return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
gr = Group('Group Number 1', "lol", "lolik", "bolik", "python")
gr.add_student(st1)

gr.find_student('Jobs2')  # None
# gr.delete_student('Taylor')
