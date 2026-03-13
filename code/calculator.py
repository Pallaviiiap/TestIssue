def divide(a, b):
    return a / b


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = divide(a, b)

    print("Result:", result)


if __name__ == "__main__":
    main()