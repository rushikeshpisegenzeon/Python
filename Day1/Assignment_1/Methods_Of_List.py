
#append is used for adding element in list at the end
l=['rushikesh']
l.append('Pise')
print(l)

#maximum element from list
num = [2,4,56,76]
print(max(num))

#minimum element number from the list
num = [2,4,56,76]
print(min(num))

#insert at desired position
l.insert(1,'Vinayak')
print(l)

#index of element
print(num.index(76))

#reverse the list
num.reverse()
print(num)

#sort the list
num.sort()
print(num)

#remove the element
l.remove("Vinayak")
print(l)

#pop()
list = [3,4,5,4,1,4,4,4,2,3,6,7,8]
list.pop()
print(list)

#count
print(list.count(4))

#clear
l.clear()
print(l)