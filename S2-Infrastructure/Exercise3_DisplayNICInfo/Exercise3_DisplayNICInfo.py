import platform
import time
from subprocess import PIPE, run


def windows():
    our_command = "ipconfig /all"
    result = run(our_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.stdout, result.stderr)


def linux():
    our_command = "ifconfig"
    result = run(our_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.stdout, result.stderr)


def mac():
    our_command = "ifconfig"
    result = run(our_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.stdout, result.stderr)


current_platform = platform.platform()
print(current_platform)
time.sleep(2)

if current_platform.startswith("Windows"):
    windows()
elif current_platform.startswith("Linux"):
    linux()
elif current_platform.startswith("mac"):
    mac()
else:
    print("Operating System not configured!")
