
str = input("Enter the string : ")
str1=str.lower()
x = str1.count(str1[0])
y=str1.count(str1[-1])
if x==y/2 :
    print("Yes it is similar")
else :
    print("No its not similar")