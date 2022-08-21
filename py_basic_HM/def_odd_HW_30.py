def even(x):
	y = x >> 1
	if x==(y << 1):
		return True
	else:
		return False


def count(end, func):
	result = func(end)
	yield result


print(list(count(900, even)))
