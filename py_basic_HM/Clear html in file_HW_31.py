from bs4 import BeautifulSoup


def html(name, clean):
	with open(name, "r") as file:
		contents = file.read()
		soup = BeautifulSoup(contents, 'lxml')
		title = soup.text
		file = open(clean, 'w')
		file.write(title)
		file.close()
		return soup


name = input("Absolute path ot file: ")
clean = input("Name of cleaned file: ")

print(html(name, clean))
