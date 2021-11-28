import random


def choice():
    while True:
        try:
            player_choice = int(input("Choice: "))
            if player_choice < 1 or player_choice > 2:
                raise ValueError("Please enter a number between 0 and 20")
        except ValueError:
            print("Please enter 1 or 2")
            continue

        if player_choice == 1:
            guess_number()
        elif player_choice == 2:
            exit()


def guess_number():
    print("\n\033[1mGenerating number, please wait!\033[0m")
    random_number = random.randint(0, 20)

    while True:
        try:
            user_input = int(input("Guess the number between 0 and 20: "))
            if user_input < 0 or user_input > 20:
                raise ValueError("Please enter a number between 0 and 20")
        except ValueError:
            print("Please enter a number between 0 and 20\n")
            continue
        if user_input == random_number:
            print("Yes! You guessed the right number!")

            print("\n\nPlease select a number!")
            print("1 - Try Again")
            print("2 - Exit")

            try:
                choice()
            except ValueError:
                print("Something went wrong")
        else:
            print("Please try again\n")


guess_number()
