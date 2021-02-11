# ========================================= #
# Author: Luke Hendriks

# Imports
import socket
import pyfiglet
import argparse
import sys
from datetime import *


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


###########################################################################
# ============================ Start Screen ============================= #
###########################################################################
def start_screen():
    def banner():
        banner = pyfiglet.figlet_format("Port Scanner")
        print(banner)
        print("Welcome to my Port Scanner!\n")

    def arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('target', action="store", type=str,
                            help="IP-address or domain name of the host to scan.")
        parser.add_argument('minport', action="store", type=int, help="Minimum port to check.")
        parser.add_argument('maxport', action="store", type=int, help="Maximum port to check.")
        parser.add_argument('debug', action="store", type=str, help="Enable or disable debug mode. Enter y or n")
        args = parser.parse_args()
        return args

    def check_input():
        if args.minport < 1 or args.minport > 65535:
            print("MinPort Must be between 1 and 65535!")
            sys.exit()
        if args.maxport < 1 or args.maxport > 65535:
            print("MaxPort Must be between 1 and 65535!")
            sys.exit()
        if args.minport > args.maxport:
            print("MinPort must be lower than MaxPort!")
            sys.exit()

    args = arguments()
    banner()
    check_input()

    if args.debug == "y":
        print("You arguments: ")
        print("     IP-Address: " + args.target)
        print("     Min-Port: " + str(args.minport))
        print("     Max-Port: " + str(args.maxport))
        print("     Debug: " + str(args.debug) + "\n")

    scan_ports(args.target, args.minport, args.maxport, args.debug)


###########################################################################
# =========================== Scan for ports ============================ #
###########################################################################
def scan_ports(target, minport, maxport, debug):
    def summary():
        current_date = date.today()
        current_time = datetime.now()
        date_to_write = str(current_date.strftime("%d-%m-%Y")) + " " + str(current_time.strftime("%H:%M:%S"))

        with open(target + ".txt", "a") as f:
            f.write("# =========================== Port Scan ============================ #" + "\n")
            f.write("Target Host: " + target + "\n")
            f.write("Datetime: " + date_to_write + "\n\n")
            f.write("Summary:" + "\n")
            f.write("   Open Ports: " + str(open_ports) + "\n")
            f.write("   Closed Ports: " + str(closed_ports) + "\n\n\n")

    port_to_check = minport
    print("Scanning Ports, Please wait!\n")
    open_ports = []
    closed_ports = []
    while True:
        if port_to_check < maxport + 1:
            try:
                socket.create_connection((target, port_to_check), 1)
                open_ports.append(port_to_check)
                if debug == "y":
                    print("Port " + str(port_to_check) + " open")
                port_to_check += 1
            except socket.timeout as tmo:
                closed_ports.append(port_to_check)
                if debug == "y":
                    print("Port: " + str(port_to_check) + " " + str(tmo))
                port_to_check += 1
            except socket.error as err:
                closed_ports.append(port_to_check)
                if debug == "y":
                    print("Port: " + str(port_to_check) + " " + str(err))
                port_to_check += 1
        else:
            summary()
            print("\nDone Scanning Ports! View file named " + target + ".txt for summary! Exiting Program!")
            sys.exit()


start_screen()
