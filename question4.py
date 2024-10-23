# Taking input from the user
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Performing the operation
if operation == '+':
    answer = number1 + number2
elif operation == '-':
    answer = number1 - number2
elif operation == '*':
    answer = number1 * number2
elif operation == '/':
    if number2 != 0:
        answer = number1 / number2
    else:
        answer = "Error! Can't be divided by zero."
else:
    answer = "Invalid operation!"

# Printing the result
print("Answer:", answer)