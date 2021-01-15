# Mon1 Code

# Imports
from datetime import *
import platform
import psutil

# Global variables
global usage_path

# === GLOBAL === #
# Get Current Date
current_date = date.today()
current_time = datetime.now()

date_to_write = "Date: " + str(current_date.strftime("%Y-%m-%d")) + str(current_time.strftime("%H:%M:%S"))

# Get System Info
platform_info = platform.uname()

system_os = platform_info.system + " " + platform_info.version
system_name = platform_info.node

host_to_write = "Host: " + system_name
os_to_write = "OS:   " + system_os


# === HARDWARE === #
# Get CPU Usage
def cpu(file):
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()

    cpu_freq_current = psutil.cpu_freq().current
    cpu_freq_min = psutil.cpu_freq().min
    cpu_freq_max = psutil.cpu_freq().max

    cpu_to_write1 = "Cores: " + str(cpu_cores) + " | Threads: " + str(cpu_threads) + " | Percent used: " + str(
        cpu_percent) + "%"
    file.write("\n" + cpu_to_write1)

    cpu_to_write2 = "Current Frequency: " + str(cpu_freq_current) + " | Min Frequency: " + str(cpu_freq_min) + \
                    " | Max Frequency: " + str(cpu_freq_max)
    file.write("\n" + cpu_to_write2)


# Get Hard disk Usage
def disk(file):
    global usage_path
    if platform_info.system == "Windows":
        usage_path = "C:\\"
    elif platform_info.system == "Linux":
        usage_path = "/"
    elif platform_info.system == "mac":
        usage_path = "/"

    disk_usage = psutil.disk_usage(path=usage_path)
    disk_io = psutil.disk_io_counters(perdisk=True)

    total_disk_usage = disk_usage.total / (2 ** 30)
    used_disk_usage = disk_usage.used / (2 ** 30)
    free_disk_usage = disk_usage.free / (2 ** 30)
    disk_percent = disk_usage.percent

    disk_to_write = "Total disk: " + str(round(total_disk_usage, 1)) + "GB" + " | Used disk: " + str(
        round(used_disk_usage, 1)) + "GB" + " | Free disk: " + str(
        round(free_disk_usage, 1)) + "GB" + " | Percent used: " + str(round(disk_percent, 1)) + "%" + "\n"
    file.write("\n" + disk_to_write)

    for x in disk_io:
        io_to_write = x + " { Read_bytes:" + str(disk_io[x].read_bytes) + " | Write_bytes:" + str(
            disk_io[x].write_bytes) + " | Read_time:" + str(disk_io[x].read_time) + " | Write_time:" + str(
            disk_io[x].write_time) + " }"
        file.write("\n" + io_to_write)


# Get RAM Usage
def ram(file):
    memory_usage = psutil.virtual_memory()
    total_memory_usage = memory_usage.total / (2 ** 30)
    used_memory_usage = memory_usage.used / (2 ** 30)
    free_memory_usage = memory_usage.available / (2 ** 30)
    memory_percent = memory_usage.percent

    ram_to_write = "Total memory: " + str(round(total_memory_usage, 1)) + "GB" + " | Used memory: " + str(
        round(used_memory_usage, 1)) + "GB" + " | Free memory: " + str(
        round(free_memory_usage, 1)) + "GB" + " | Percent used: " + str(round(memory_percent, 1)) + "%"
    file.write("\n" + ram_to_write)


def write_file():
    file_to_create = current_date.strftime("%Y-%m-%d") + current_time.strftime("T%H%M%S") + ".txt"

    f = open(file_to_create, "w")
    f.write(date_to_write + "\n")
    f.write(host_to_write + "\n")
    f.write(os_to_write + "\n")

    f.write("\n")
    f.write(40 * "=" + " CPU " + 40 * "=")
    cpu(f)

    f.write("\n\n")
    f.write(40 * "=" + " DISK " + 40 * "=")
    disk(f)

    f.write("\n\n")
    f.write(40 * "=" + " RAM " + 40 * "=")
    ram(f)


write_file()
