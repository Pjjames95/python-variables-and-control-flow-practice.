# Taking the lengths of the three sides as input
side1 = int(input("Enter the length of first side: "))
side2 = int(input("Enter the length of  second side: "))
side3 = int(input("Enter the length of  third side: "))

# Determining the type of triangle
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")