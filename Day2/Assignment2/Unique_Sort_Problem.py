
#Type1
_list = input("Enter the list ")
clr_list =set(_list.split(','))
print("Unsorted but unique list : ",clr_list)
sorted_list=list(clr_list)
sorted_list.sort()
print("Sorted list : ",sorted_list)


#Type2
_list = input("Enter the list ")
clr_list =_list.split(',')
new_list = sorted(set(clr_list))
print("Type2 output : ",new_list)