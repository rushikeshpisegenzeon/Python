from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda x:x%2==0,nums))
print(evens)
double = list(map(lambda x:x*2,evens))
print(double)
sum = reduce(lambda a,b:a+b,double)
print(sum)