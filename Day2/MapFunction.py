list_ = ["hello","HI","good"]

print(list(map(lambda x:x.upper(),list_)))

myl=[9,25,50,3,8,8]
odd_numbers = list(filter(lambda x: x % 2 == 1, myl))

print(odd_numbers)