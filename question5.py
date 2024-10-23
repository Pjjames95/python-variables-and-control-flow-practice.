def age_derteminer(age):
    if age < 18:
        print("minor")
    elif 18 <= age <= 65:
        print("adult")
    else:
        print("senior")
age= int(input("Enter your age:"))
age_derteminer(age)
