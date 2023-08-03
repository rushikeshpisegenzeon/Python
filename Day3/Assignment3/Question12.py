def capatlised_list_elements(list_):
    capatlised_list = list(map(lambda x:x.capitalize(),list_))
    return capatlised_list


def write_list_to_file(param, capatilised_list):
    with open("listupper.txt","w") as file:
        for item in capatilised_list:
            file.write(item + "\n")



def main():
    try:
        list_ = input("Enter the list of strings(with comma seprator) : ")
        _list_=list_.split(",")
        capatlised_list = capatlised_list_elements(_list_)
        write_list_to_file("listupper.txt",capatlised_list)
        print("List elements capitalized and written to listupper.txt")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()