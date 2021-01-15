import re


# Get input from the user, his or her password.
def passwordchecker():
    while True:
        try:
            firstName = input("Please insert your first name here: ")
            try:
                val = int(firstName)
                q = 1
            except:
                q = 0

            if not firstName or q == 1:
                raise ValueError("Please enter your first name!")
            break
        except ValueError as a:
            print(a)
            continue

    while True:
        try:
            lastName = input("Please insert your last name here: ")
            try:
                val = int(lastName)
                q = 1
            except:
                q = 0
            if not lastName or q == 1:
                raise ValueError("Please enter your last name!")
            break
        except ValueError as b:
            print(b)
            continue

    while True:
        try:
            age = input("Please insert your age here: ")
            break
        except:
            print("Please enter your age")
            continue

    password = input("Please insert your password here: ")
    x = 0
    # Check the password, is it using normal letters, capital letters, numbers an symbols?
    # If it passes on of the requirements, add +1 to x.
    if len(password) >= 8:
        x += 1
    if re.search("[a-z]", password):
        x += 1
    if re.search("[A-Z]", password):
        x += 1
    if re.search("[0-9]", password):
        x += 1
    if re.search("[_@#]", password):
        x += 1
    if firstName in password:
        x -= 1
    if lastName in password:
        x -= 1
    if age in password:
        x -= 1

    # Check x, how many requirements does the password pass?
    # Based on that answer is the password very weak, weak, good, strong or very strong?
    if x == 0 or x == 1:
        print("This password is very weak!")
    if x == 2:
        print("This password is weak!")
    if x == 3:
        print("This password is good!")
    if x == 4:
        print("This password is strong!")
    if x == 5:
        print("This password is very strong!")


# Run function
passwordchecker()
