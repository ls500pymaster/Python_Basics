x = (1, 2, 3, 5, 5, 5, 7, 8,)
new_list = []
for num in range(0, len(x)):
	new_list.append(x[num] + 10)
print(new_list)
print(x)

print(x.count(5))
print(x.index(1))

t = list(x)
t[0] = 10
x = tuple(t)
print(x)

x += (9, 9)
print(x)
