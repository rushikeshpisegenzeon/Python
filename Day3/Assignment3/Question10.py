
def count_digits_and_write_to_file(number):
    try:
        num_str = str(number)
        digit_count = len(num_str)

        with open("countdigit.txt","w") as file:
            file.write(f"Number of digits in {number}: {digit_count}")

        return digit_count
    except Exception as e:
        return str(e)

def main():
    try:
        number = int(input("Enter a number : "))
        digit_count = count_digits_and_write_to_file(number)
        print(f"Number of digits: {digit_count}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()