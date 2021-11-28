from tkinter import *
from tkinter import messagebox
import random

global guesses_one_player, stripes_label_one_player, list_one_player


def one_player():
    global guesses_one_player, stripes_label_one_player, list_one_player
    possible_words = ["test", "koek"]
    chosen_word = random.choice(possible_words)
    user_guesses = []
    chosen_word_letter_list = []
    for x in chosen_word:
        chosen_word_letter_list.append(" _ ")
    list_one_player = ''.join(chosen_word_letter_list)
    guesses_one_player = len(chosen_word) + 2

    # === MAIN PROGRAM === #
    def game():
        global guesses_one_player, stripes_label_one_player, list_one_player

        game_over = False
        won = False

        if int(guesses_one_player) > 0:
            guesses_label.configure(text=guesses_one_player)
        elif guesses_one_player == 0:
            game_over = True

        if list_one_player == chosen_word.upper():
            won = True

        user_input = entry_input.get()
        if len(user_input) == len(chosen_word):
            if user_input == chosen_word:
                won = True
            else:
                guesses_one_player -= 1
                guesses_label.configure(text=guesses_one_player)
                messagebox.showinfo("", "Het door jou ingevoerde woord was onjuist!")
        elif user_input in user_guesses:
            messagebox.showinfo("", "Deze letter heb je al eens geprobeerd!")
        elif len(user_input) > 1:
            messagebox.showinfo("", "Voer alstublieft 1 letter in!")
        elif len(user_input) < 1:
            messagebox.showinfo("", "Voer alstublieft 1 letter in!")
        else:
            user_guesses.append(user_input)
            if user_input in chosen_word:
                for i in range(len(chosen_word)):
                    if user_input == chosen_word[i]:
                        LetterIndex = i
                        chosen_word_letter_list[LetterIndex] = user_input.upper()
                        list_one_player = ''.join(chosen_word_letter_list)
                        stripes_label_one_player.configure(text=list_one_player)
            else:
                guesses_one_player -= 1
                guesses_label.configure(text=guesses_one_player)
                messagebox.showinfo("", "Het te raden woord bevat geen " + user_input)

        entry_input.delete(0, "end")

        if int(guesses_one_player) > 0:
            guesses_label.configure(text=guesses_one_player)
        elif guesses_one_player == 0:
            game_over = True

        if list_one_player == chosen_word.upper():
            won = True

        if won:
            stripes_label_one_player = Label(one_player_screen, text="Je hebt gewonnen!", font=('Courier', 50))
            stripes_label_one_player.grid(row=1, column=2)
            insert_guess_btn.destroy()
            entry_input.destroy()
            guesses_label.destroy()
            one_player_screen.mainloop()
        if game_over:
            stripes_label_one_player = Label(one_player_screen, text="Helaas, je hebt verloren!", font=('Courier', 50))
            stripes_label_one_player.grid(row=1, column=2)
            insert_guess_btn.destroy()
            entry_input.destroy()
            guesses_label.destroy()
            one_player_screen.mainloop()

    one_player_screen = Tk()
    one_player_screen.title("Galgje")
    one_player_screen.geometry("+0+0")

    # ICONS
    home_icon = PhotoImage(file="Home_icon.png")

    # LABELS
    guesses_label = Label(one_player_screen, text=guesses_one_player, font=('Courier', 50))
    guesses_label.grid(row=1, column=4)
    stripes_label_one_player = Label(one_player_screen, text=list_one_player, font=('Courier', 50))
    stripes_label_one_player.grid(row=1, column=2)

    # BUTTONS
    main_menu_screen_button = Button(one_player_screen, text="Home", image=home_icon, height=75, width=75,
                                     command=lambda: [one_player_screen.destroy(), main_menu()])
    main_menu_screen_button.grid(row=1, column=1)
    insert_guess_btn = Button(one_player_screen, text="Insert Guess", command=game, font=('Courier', 45))
    insert_guess_btn.grid(row=4, column=1, columnspan=15, sticky=W + E)

    # ENTRY
    entry_input = Entry(one_player_screen, font=('Courier', 45), width=5)
    entry_input.grid(row=3, column=2, columnspan=1, sticky=W + E, pady=30)

    one_player_screen.mainloop()


def main_menu():
    main_menu_screen = Tk()
    main_menu_screen.title("Galgje")
    main_menu_screen.geometry("+0+0")

    # === MAIN MENU SCREEN === #
    # LABELS
    label_title = Label(main_menu_screen, text="Galgje", font=('Courier', 60))
    label_title.grid(sticky=E + W + N, columnspan=2)
    label_info1 = Label(main_menu_screen, text="Het Beroemde Galgje!", font=('Courier', 25))
    label_info1.grid(columnspan=2)
    label_info2 = Label(main_menu_screen,
                        text="1 Speler: Er wordt een woord gekozen, probeer deze te raden voordat het te laat is!",
                        font=('Courier', 15))
    label_info2.grid(columnspan=2)
    label_info3 = Label(main_menu_screen, text="2 Spelers: Een speler geeft een woord, de ander moet dit woord raden. "
                                               "Wie heeft de tegensstander zijn of haar woord het snelste geraden?",
                        font=('Courier', 15))
    label_info3.grid(columnspan=2)

    # BUTTONS
    btn_1player = Button(main_menu_screen, text="1 Speler", font=('Courier', 60),
                         command=lambda: [main_menu_screen.destroy(), one_player()])
    btn_1player.grid(row=4, sticky=W + E, column=0, columnspan=3, pady=(50, 0))

    main_menu_screen.mainloop()


main_menu()
