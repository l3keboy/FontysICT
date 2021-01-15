from tkinter import *
from tkinter import messagebox
from progress.bar import Bar
import time

objects = []


# === CLASSES === #
class EntityDisplay:
    # === FUNCTIONS === #
    def __init__(self, master, s, u, p, i):
        self.password = p
        self.site = s
        self.username = u
        self.window = master
        self.i = i

        # Decrypt the password back to normal.
        decrypted_site = ""
        decrypted_username = ""
        decrypted_password = ""
        for letter in self.site:
            if letter == ' ':
                decrypted_site += ' '
            else:
                decrypted_site += chr(ord(letter) - 5)

        for letter in self.username:
            if letter == ' ':
                decrypted_username += ' '
            else:
                decrypted_username += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                decrypted_password += ' '
            else:
                decrypted_password += chr(ord(letter) - 5)

        # Add decrypted text to a label.
        self.label_site = Label(self.window, text=decrypted_site, font='Courier')
        self.label_username = Label(self.window, text=decrypted_username, font='Courier')
        self.label_password = Label(self.window, text=decrypted_password, font='Courier')

    def display(self):
        # Display the made labels.
        self.label_site.grid(row=6 + self.i, column=1)
        self.label_username.grid(row=6 + self.i, column=2)
        self.label_password.grid(row=6 + self.i, column=3)


# === FUNCTIONS === #
def progress_bar():
    # Run via CMD for progress bar.
    bar = Bar('Logging in!', max=20)
    for i in range(20):
        bar.next()
        time.sleep(0.02)
    bar.finish()


def validation():
    # === FUNCTIONS === #
    def try_login():
        if entry_validation.get() == "Doemaarwat1":
            progress_bar()
            validation_screen.destroy()
            startup_screen()
        else:
            messagebox.showinfo("Login", "Wrong password!")

    # === VALIDATION SCREEN LOOK + FUNCTIONALITY === #
    validation_screen = Tk()
    validation_screen.geometry("256x116")
    validation_screen.title("Username and password saver")

    label_validation = Label(validation_screen, text="Password:", font=('Courier', 14))
    label_validation.grid(row=1, column=1)
    entry_validation = Entry(validation_screen, width=42)
    entry_validation.grid(row=2, columnspan=3, ipady=5)
    btn_login = Button(validation_screen, text="Login", command=try_login, height=2, font=('Courier', 14))
    btn_login.grid(row=4, columnspan=3, sticky=E + W)

    validation_screen.mainloop()


def startup_screen():
    # === FUNCTIONS === #
    def submit():
        file = open("passwords.txt", "a")
        # Check if site message box is empty, if so don't input, instead give message box with the error.
        if entry_site.index("end") == 0:
            messagebox.showinfo("Site", "Site name is empty!")
        # Check if username message box is empty, if so don't input, instead give message box with the error.
        elif entry_username.index("end") == 0:
            messagebox.showinfo("Username", "Username is empty!")
        # Check if password message box is empty, if so don't input, instead give message box with the error.
        elif entry_passwd.index("end") == 0:
            messagebox.showinfo("Password", "Password is empty!")
        # If all message boxes are filled in, add low level encryption and write to the document passwords.txt.
        else:
            # Encrypt input site.
            input_site = entry_site.get()
            encrypted_site = ''
            for letter in input_site:
                if letter == ' ':
                    encrypted_site += ' '
                else:
                    encrypted_site += chr(ord(letter) + 5)

            # Encrypt input username.
            input_username = entry_username.get()
            encrypted_username = ''
            for letter in input_username:
                if letter == ' ':
                    encrypted_username += ' '
                else:
                    encrypted_username += chr(ord(letter) + 5)

            # Encrypt input password.
            input_passwd = entry_passwd.get()
            encrypted_passwd = ''
            for letter in input_passwd:
                if letter == ' ':
                    encrypted_passwd += ' '
                else:
                    encrypted_passwd += chr(ord(letter) + 5)
            # Write to file and close file.
            file.write(encrypted_site + ',' + encrypted_username + ',' + encrypted_passwd + ', \n')
            file.close()

    # === STARTUP SCREEN LOOK + FUNCTIONALITY === #
    main_screen = Tk()
    main_screen.geometry("362x199")
    main_screen.title("Username and password saver")

    # === LABELS === #
    label_site = Label(main_screen, text="Site Name:", font=('Courier', 14))
    label_site.grid(row=1, column=0)
    label_username = Label(main_screen, text=" Username:", font=('Courier', 14))
    label_username.grid(row=2, column=0)
    label_passwd = Label(main_screen, text=" Password:", font=('Courier', 14))
    label_passwd.grid(row=3, column=0)

    # === ENTRY BOXES === #
    entry_site = Entry(main_screen, width=40)
    entry_site.grid(row=1, column=1)
    entry_username = Entry(main_screen, width=40)
    entry_username.grid(row=2, column=1)
    entry_passwd = Entry(main_screen, width=40)
    entry_passwd.grid(row=3, column=1)

    # === BUTTONS === #
    btn_submit = Button(main_screen, text="Submit", width=26, height=2, command=submit, font=('Courier', 14))
    btn_submit.grid(row=4, columnspan=5, sticky=E + W)

    btn_passwdview = Button(main_screen, text="View Passwords", width=26, height=2,
                            command=lambda: [main_screen.destroy(), view_passwd_screen()], font=('Courier', 14))
    btn_passwdview.grid(row=5, columnspan=5, sticky=E + W)

    main_screen.mainloop()


def view_passwd_screen():
    # === VIEW PASSWORD SCREEN LOOK + FUNCTIONALITY === #
    passwd_screen = Tk()
    passwd_screen.title("Username and password saver")

    # === LABELS === #
    label_site = Label(passwd_screen, text="Site Name:", font=('Courier', 14))
    label_site.grid(row=2, column=1)
    label_username = Label(passwd_screen, text="Username:", font=('Courier', 14))
    label_username.grid(row=2, column=2)
    label_password = Label(passwd_screen, text="Password:", font=('Courier', 14))
    label_password.grid(row=2, column=3)

    # Open the passwords.txt file, read the lines en split by comma.
    f = open('passwords.txt', 'r')
    count = 0
    for line in f:
        entity_list = line.split(',')
        e = EntityDisplay(passwd_screen, entity_list[0], entity_list[1], entity_list[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()

    # === BUTTONS === #
    btn_main_screen_view = Button(passwd_screen, text="View main screen", height=2,
                                  command=lambda: [passwd_screen.destroy(), startup_screen()], font=('Courier', 14))
    btn_main_screen_view.grid(row=1, columnspan=4, sticky=E + W)

    passwd_screen.mainloop()


# Start program by running validation function.
validation()
