def add_one(a):
	if a < 2:
		return False
	for i in range(2, int(a ** 0.5 + 1)):
		if a % i==0:
			return False
	else:
		return a


def count(start, end, func):
	for i in range(end):
		start = start + 1
		result = func(start)
		yield result


print(list(count(1, 15, add_one)))
