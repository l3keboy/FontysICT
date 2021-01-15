import string
import random

# Get input from the user.
# In this case an int, which is used for password length.
while True:
    try:
        password_length = int(input("Please enter a number, this will be the length of your password: "))
        if password_length < 0:
            raise ValueError("Please enter a valid number!")
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Generate a random password.
    def generate_password(length_password):
        password = ''

        for x in range(length_password):
            p = random.randint(0, 90)
            password += string.printable[p]

        # Return the generated password.
        return password


    # Show password
    print("\nUw wachtwoord is: " + generate_password(password_length))
    exit()
