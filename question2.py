def number_type(number):
    # Checking if the number is even or odd
    if number / 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
        # Asking the user for a number
number = int(input("Enter a number: "))
number_type(number)
