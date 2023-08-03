def reverse_string(input_string):
    return input_string[::-1]


def main():
    try:
         with open("stringinput.txt","r") as input_file:
             input_string= input_file.read().strip()

         reversed_string = reverse_string(input_string)

         with open("reversestr.txt", "w") as output_file:
              output_file.write(reversed_string)

         print("String reversed and written to the file reversestr.txt")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()