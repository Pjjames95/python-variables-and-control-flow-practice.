def week_days(day_number):
    if day_number == 1:
        print("Monday")
    elif day_number == 2:
        print("Tuesday")
    elif day_number == 3:
        print("Wednesday")
    elif day_number == 4:
        print("Thursday")
    elif day_number == 5:
        print("Friday")
    elif day_number == 6:
        print("Saturday")
    elif day_number == 7:
        print("Sunday")
    else:
        print("Invalid input.")
day_number = int(input("Enter a number please:"))
week_days(day_number)