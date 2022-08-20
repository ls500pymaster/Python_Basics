def cube(end):
	for num in range(2, end):
		cube = num ** 3
		if cube < end:
			yield cube


print(list(cube(100)))
