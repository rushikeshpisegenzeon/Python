
set1 = {33,44,22,1,54,56}

#add the element in set
set1.add(77)
print("set1 ",set1)

#copy
set2 = set1.copy()
print("set2 ",set2)

#difference
set3 = {12,32,11,77,22,33,44}
print("set3 ",set3)
print("difference of set1 to set3",set1.difference(set3))
print("difference of set3 to set1",set3.difference(set1))

#intersection
print("intersection",set2.intersection(set3))

#isSubset
set4={32,33}
print(set4.issubset(set3))

#isSuperSet
print((set3.issuperset(set4)))

#Union
print("union",set1.union(set3))

#update
set5={67,88}
set1.update(set5)
print(set1)