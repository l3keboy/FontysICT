import platform  # Get platform information.
import psutil  # Get info about components.
import time  # Stop the code for x amount of time.


# Get system info.
def system():
    platform_info = platform.uname()

    print("=" * 40, "System Info", "=" * 40)
    print("\033[1mComputer Name: \033[0m", end=""), print(platform_info.node)
    print("\033[1mSystem: \033[0m", end=""), print(platform_info.system)
    print("\033[1mVersion: \033[0m", end=""), print(platform_info.version)


# Get CPU info.
def cpu():
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count()
    cpu_stats = psutil.cpu_percent()

    print("=" * 40, "CPU Info", "=" * 40)
    print("\033[1mThe number of cores is: \033[0m", end=""), print(cpu_cores)
    print("\033[1mThe number of threads is: \033[0m", end=""), print(cpu_threads)
    print("\033[1mYour CPU percentage is: \033[0m", end=""), print(cpu_stats, end=""), print("%")


# Get Disk info.
def disk():
    disk_usage = psutil.disk_usage(path="C:\\")
    total_disk_usage = disk_usage.total / (2 ** 30)
    used_disk_usage = disk_usage.used / (2 ** 30)
    free_disk_usage = disk_usage.free / (2 ** 30)

    print("=" * 40, "Disk Info", "=" * 40)
    print("\033[1mTotal: \033[0m", end=""), print(round(total_disk_usage, 1), end=""), print(" Gigabyte")
    print("\033[1mUsed: \033[0m", end=""), print(round(used_disk_usage, 1), end=""), print(" Gigabyte")
    print("\033[1mFree: \033[0m", end=""), print(round(free_disk_usage, 1), end=""), print(" Gigabyte\n")
    print("\033[1mPercent used: \033[0m", end=""), print(round(disk_usage.percent, 1), end=""), print("%")


# Get Memory info
def memory():
    memory_usage = psutil.virtual_memory()
    total_memory_usage = memory_usage.total / (2 ** 30)
    used_memory_usage = memory_usage.used / (2 ** 30)
    free_memory_usage = memory_usage.available / (2 ** 30)

    print("=" * 40, "Memory Info", "=" * 40)
    print("\033[1mTotal: \033[0m", end=""), print(round(total_memory_usage, 1), end=""), print(" Gigabyte")
    print("\033[1mUsed: \033[0m", end=""), print(round(used_memory_usage, 1), end=""), print(" Gigabyte")
    print("\033[1mFree: \033[0m", end=""), print(round(free_memory_usage, 1), end=""), print(" Gigabyte\n")
    print("\033[1mPercent used: \033[0m", end=""), print(memory_usage.percent, end=""), print("%")


while True:
    try:
        print("\nPlease select the component you want to see. \n")
        print("            1 - System Info")
        print("            2 - CPU Info")
        print("            3 - Disk Info")
        print("            4 - Memory Info\n")
        menu_screen = int(input("Number: "))
        if menu_screen < 0:
            raise ValueError("Please insert a valid number")
    except ValueError:
        print("Please insert a valid number!")
        continue

    if menu_screen == 1:  # If input = 1.
        system()  # Run system function.
        time.sleep(2)  # Stop code for 2 seconds.
    elif menu_screen == 2:  # If input = 2.
        cpu()  # Run cpu function.
        time.sleep(3)  # Stop code for 3 seconds.
    elif menu_screen == 3:  # If input = 3.
        disk()  # Run disk function.
        time.sleep(5)  # Stop code for 5 seconds.
    elif menu_screen == 4:  # If input = 4.
        memory()  # Run memory function.
        time.sleep(5)  # Stop code for 5 seconds.
    continue
