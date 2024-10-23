def password_derterminer(password):
    # Checking the password
    if password == "python123":
        print("Access granted.")
    else:
        print("Access denied.")
password = input("Please enter your password:")
password_derterminer(password)