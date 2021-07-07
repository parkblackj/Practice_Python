from functools import reduce

int_numbers = range(-5, 6)

numbers = filter(lambda x: x > 0, int_numbers)

print(numbers)
print(list(numbers))

numbers = map(lambda x: x * 2, int_numbers)

print(numbers)
print(list(numbers))

lst = {1, 2, 3, 4}

lst_1 = reduce(lambda x, y: x*y, lst)
print(lst_1)
