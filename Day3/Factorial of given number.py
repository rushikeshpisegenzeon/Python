def fact(x):
    if x==0 :
        return 1
    return  x * fact(x-1)



x = int(input("ENter the number which you want to factorial "))
result = fact(x)
print(result)