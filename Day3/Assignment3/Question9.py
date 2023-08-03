class InvalidProductBillException(Exception):
    def __init__(self, cost):
        self.cost = cost
        super().__init__(f"Bill cannot be negative: {cost}")


def main():
    try:
        cost = int(input("Enter the cost: "))
        if cost < 0:
            raise InvalidProductBillException(cost)
        else:
            print("Bill is valid.")
    except ValueError:
        print("Invalid input. Please enter a valid cost.")
    except InvalidProductBillException as e:
        print(e)


if __name__ == "__main__":
    main()
