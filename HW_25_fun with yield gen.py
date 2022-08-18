def add_one(value):
    return value ** 2

def count(start, end, func):
    while end < 15:
        yield start
        end += 1
        start = func(start)

print(list(count(2, 10, add_one)))