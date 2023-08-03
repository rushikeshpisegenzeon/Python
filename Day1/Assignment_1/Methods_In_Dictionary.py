
dic = {"Dev":"abc","QA":"pqr","BA":"xyz"}

# get method
print(dic.get("BA"))

#get all the keys
print(dic.keys())

#get all the values
print(dic.values())

#get all the items
print(dic.items())

#copy
new_dic=dic.copy()
print("new dictionary is",new_dic)