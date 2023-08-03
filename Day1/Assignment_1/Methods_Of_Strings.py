
str = "hello i am rushikesh pise"

#Capitalized the first letter of string
temp = str.capitalize()
print(temp)

#format
fname="Rushikesh"
company="Genzeon"
age=25

str1 = "My Name is {0} i am {2} year old, and i am currently work in {1}".format(fname,company,age)
print(str1)

#islower return true or false
str3="hello"
print(str3.islower())

#isupper return true or false
str4="HELLO"
print(str4.isupper())

#length of the string using len function
print(len(str4))

#find out the index of given Character(first occurence)
print(str4.find("L"))

#find out the count of given character in entire string
print("Rushikesh Pise".count("s"))

#split the string by the the given character
print("Rushikesh vinayak pise".split(" "))

#isdigit return the true false as per the string contain digit or not
print("345a".isdigit())

