from functools import reduce


def add(a,b):
    return a+b

numbers = [25,12,33,12,8,10]

sum = reduce(add,numbers)
print(sum)