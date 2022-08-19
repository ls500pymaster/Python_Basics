def add_one(value):
    return value ** 2

def count(start, end, func):
    for element in range(end):
        yield start
        start = func(start)

print(list(count(2, 5, add_one)))