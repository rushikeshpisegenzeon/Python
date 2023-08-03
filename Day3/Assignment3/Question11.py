def sum_of_N_numbers(number):
    try:

         sum=0
         for i in range(1,number+1):
             sum+=i

         with open("sumresult.txt", "w") as file:
             file.write(f"The sum of all natural number from 1 to {number} is : {sum}")

         return sum
    except Exception as e:
        return str(e)



def main():
    try:
        number = int(input("Enter the number : "))
        sum_of_num = sum_of_N_numbers(number)
        print(f"The sum of all natural number from 1 to {number} is : {sum_of_num}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

