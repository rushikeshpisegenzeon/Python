
def custom_sort(word):
    clr_order = ["cyan", "green", "magenta", "orange", "pink", "red", "white"]
    return clr_order.index(word)



str = input("Enter a string : ")
list = str.split(',')
unique_list = sorted(set(list),custom_sort())

print("sorted values : ",unique_list)