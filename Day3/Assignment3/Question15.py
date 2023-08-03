def find_largest(numbers):
    return max(numbers)

def main():
    try:
        with open ("input.txt","r") as input_file:
            numbers = [int(num)for num in input_file.read().split()]

        if len(numbers) != 3:
            print("File should contain exactlty three numbers.")
            return

        largest = find_largest(numbers)
        with open("largest.txt", "w") as output_file:
            output_file.write(str(largest))
        print("Largest number is stored in the file largest.txt")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()