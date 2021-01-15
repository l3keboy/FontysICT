# import time
from tkinter import *
from tkinter import Tk

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import psutil
import platform
import threading


# === The Drop Down Menu === #
def drop_down_menu(screen):
    # === Drop Down Menu === #
    monitor_menu = Menu(screen)
    screen.config(menu=monitor_menu)
    sub_menu = Menu(monitor_menu)
    monitor_menu.add_cascade(label="Monitor", menu=sub_menu)
    sub_menu.add_command(label="System Information",
                         command=lambda: [screen.destroy(), draw_system_information()])
    sub_menu.add_command(label="System Performance",
                         command=lambda: [screen.destroy(), draw_system_performance()])
    sub_menu.add_command(label="CPU Information",
                         command=lambda: [screen.destroy(), draw_extended_cpu_information()])
    sub_menu.add_command(label="RAM Information",
                         command=lambda: [screen.destroy(), draw_extended_ram_information()])
    sub_menu.add_command(label="Disk Information",
                         command=lambda: [screen.destroy(), draw_extended_disk_information()])


# === Draw System Info === #
def draw_system_information():
    system_information_window = Tk()
    system_information_window.title("System Information")

    platform_info = platform.uname()

    # === Labels === #
    label_system_info_title = Label(system_information_window, text="System Information", font=("Courier", 25))
    label_system_info_title.grid(row=1, columnspan=15)

    # *** System Name *** #
    label_system_name1 = Label(system_information_window, text="System Name: ", font=("Courier", 15))
    label_system_name1.grid(row=2, column=1, sticky=E)
    label_system_name2 = Label(system_information_window, text=platform_info.node, font=("Courier", 15))
    label_system_name2.grid(row=2, column=2)

    # *** System OS *** #
    label_system_os1 = Label(system_information_window, text="Operating System: ", font=("Courier", 15))
    label_system_os1.grid(row=3, column=1, sticky=E)
    label_system_os2 = Label(system_information_window, text=platform_info.system, font=("Courier", 15))
    label_system_os2.grid(row=3, column=2)

    # *** System OS Version *** #
    label_system_os_version1 = Label(system_information_window, text="Version: ", font=("Courier", 15))
    label_system_os_version1.grid(row=4, column=1, sticky=E)
    label_system_os_version2 = Label(system_information_window, text=platform_info.version, font=("Courier", 15))
    label_system_os_version2.grid(row=4, column=2)

    # === Call Functions === #
    drop_down_menu(system_information_window)
    system_information_window.mainloop()


# === Draw System Performance === #
def draw_system_performance():
    system_performance_window = Tk()
    system_performance_window.title("System Performance")

    # === Get CPU Info === #
    def draw_cpu_percent():
        cpu_stats = psutil.cpu_percent()
        try:
            # === Labels === #
            label_cpu_usage_perf = Label(system_performance_window, text=str(cpu_stats) + "%",
                                         font=("Courier", 15), width=10)
            label_cpu_usage_perf.grid(row=2, column=2)
            threading.Timer(1, draw_cpu_percent).start()
        except Exception as e:
            print(e)

    # === Get RAM Info === #
    def draw_ram_percent():
        memory_usage = psutil.virtual_memory()
        used_memory_percent = memory_usage.percent
        try:
            # === Labels === #
            label_ram_usage_perf = Label(system_performance_window, text=str(used_memory_percent) + "%",
                                         font=("Courier", 15), width=10)
            label_ram_usage_perf.grid(row=3, column=2)
            threading.Timer(1, draw_ram_percent).start()
        except Exception as e:
            print(e)

    # === Get Disk Info === #
    def draw_disk_percent():
        disk_usage = psutil.disk_usage(path="C:\\")
        used_disk_percent = disk_usage.percent
        try:
            # === Labels === #
            label_disk_usage_perf = Label(system_performance_window, text=str(used_disk_percent) + "%",
                                          font=("Courier", 15), width=10)
            label_disk_usage_perf.grid(row=4, column=2)
            threading.Timer(1, draw_disk_percent).start()
        except Exception as e:
            print(e)

    # === Labels === #
    label_title = Label(system_performance_window, text="System Performance", font=("Courier", 25))
    label_title.grid(row=1, columnspan=15)
    label_cpu_usage = Label(system_performance_window, text="CPU Usage:", font=("Courier", 15))
    label_cpu_usage.grid(row=2, sticky=E)
    label_ram_usage = Label(system_performance_window, text="RAM Usage:", font=("Courier", 15))
    label_ram_usage.grid(row=3, sticky=E)
    label_disk_usage = Label(system_performance_window, text="Disk Usage:", font=("Courier", 15))
    label_disk_usage.grid(row=4, sticky=E)

    # === Call Functions === #
    drop_down_menu(system_performance_window)
    draw_cpu_percent()
    draw_ram_percent()
    draw_disk_percent()

    system_performance_window.mainloop()


# === Draw Extended CPU Info === #
def draw_extended_cpu_information():
    cpu_information_window = Tk()
    cpu_information_window.title("CPU Information")

    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count()

    def draw_cpu_percent():
        cpu_stats = psutil.cpu_percent()

        # === Labels === #
        try:
            label_cpu_usage_perf = Label(cpu_information_window, text=str(cpu_stats) + "%", font=("Courier", 15),
                                         width=10)
            label_cpu_usage_perf.grid(row=4, column=2)
            threading.Timer(1, draw_cpu_percent).start()
        except Exception as e:
            print(e)

    def draw_cpu_cores_threads():

        try:
            # === Cores === #
            label_cores1 = Label(cpu_information_window, text="The number of cores is: ", font=("Courier", 15))
            label_cores1.grid(row=2, sticky=E)
            label_cores2 = Label(cpu_information_window, text=cpu_cores, font=("Courier", 15))
            label_cores2.grid(row=2, column=2)

            # === Threads === #
            label_threads1 = Label(cpu_information_window, text="The number of threads is: ", font=("Courier", 15))
            label_threads1.grid(row=3, sticky=E)
            label_threads2 = Label(cpu_information_window, text=cpu_threads, font=("Courier", 15))
            label_threads2.grid(row=3, column=2)

            threading.Timer(1, draw_cpu_cores_threads).start()
        except Exception as e:
            print(e)

    # def draw_graph():
    #     fig = plt.figure(figsize=None, dpi=None)
    #     sub_plot = fig.add_subplot(111)
    #     fig.show()
    #
    #     i = 0
    #     x, y = [], []
    #     while True:
    #         if len(x) >= 20:
    #             del x[0]
    #         if len(y) >= 20:
    #             del y[0]
    #
    #         x.append(i)
    #         y.append(psutil.cpu_percent())
    #         sub_plot.clear()
    #         sub_plot.plot(x, y)
    #         sub_plot.set_ylim(top=100, bottom=0)
    #         sub_plot.set_xlim(left=max(0, i - 10), right=i)
    #         fig.canvas.draw()
    #
    #         print(len(x), len(y))
    #         print(x)
    #         print(y)
    #
    #         i += 1
    #         time.sleep(0.5)

    # === Labels === #
    label_extended_cpu_title = Label(cpu_information_window, text="CPU Information", font=("Courier", 25))
    label_extended_cpu_title.grid(row=1, columnspan=15)
    label_cpu_usage = Label(cpu_information_window, text="CPU usage: ", font=("Courier", 15))
    label_cpu_usage.grid(row=4, sticky=E)
    # btn_graph = Button(cpu_information_window, text="Graph", width=26, height=2,
    #                    command=lambda: [cpu_information_window.destroy(), draw_graph()], font=('Courier', 15))
    # btn_graph.grid(row=5, columnspan=5, sticky=E + W)

    # === Call Functions === #
    drop_down_menu(cpu_information_window)
    draw_cpu_cores_threads()
    draw_cpu_percent()
    cpu_information_window.mainloop()


# === Draw Extended RAM Info === #
def draw_extended_ram_information():
    ram_information_window = Tk()
    ram_information_window.title("RAM Information")

    def draw_ram_percent():
        memory_usage = psutil.virtual_memory()
        used_memory_percent = memory_usage.percent

        try:
            # === Labels === #
            label_ram_usage_perf = Label(ram_information_window, text=str(used_memory_percent) + "%",
                                         font=("Courier", 15), width=10)
            label_ram_usage_perf.grid(row=5, column=2)
            threading.Timer(1, draw_ram_percent).start()
        except Exception as e:
            print(e)

    def draw_ram_total_used_free():
        memory_usage = psutil.virtual_memory()
        total_memory_usage = memory_usage.total / (2 ** 30)
        used_memory_usage = memory_usage.used / (2 ** 30)
        free_memory_usage = memory_usage.available / (2 ** 30)

        try:
            # === Total RAM === #
            label_total_ram2 = Label(ram_information_window, text=str(round(total_memory_usage, 1)) + " GB",
                                     font=("Courier", 15), width=10)
            label_total_ram2.grid(row=2, column=2)

            # === Used RAM === #
            label_used_ram2 = Label(ram_information_window, text=str(round(used_memory_usage, 1)) + " GB",
                                    font=("Courier", 15), width=10)
            label_used_ram2.grid(row=3, column=2)

            # === Free RAM === #
            label_free_ram2 = Label(ram_information_window, text=str(round(free_memory_usage, 1)) + " GB",
                                    font=("Courier", 15), width=10)
            label_free_ram2.grid(row=4, column=2)
            threading.Timer(1, draw_ram_total_used_free).start()
        except Exception as e:
            print(e)

    # === Labels === #
    label_extended_ram_title = Label(ram_information_window, text="RAM Information", font=("Courier", 25))
    label_extended_ram_title.grid(row=1, columnspan=15)

    label_total_ram1 = Label(ram_information_window, text="Total RAM: ", font=("Courier", 15))
    label_total_ram1.grid(row=2, sticky=E)
    label_used_ram1 = Label(ram_information_window, text="Used RAM: ", font=("Courier", 15))
    label_used_ram1.grid(row=3, sticky=E)
    label_free_ram1 = Label(ram_information_window, text="Free RAM: ", font=("Courier", 15))
    label_free_ram1.grid(row=4, sticky=E)
    label_ram_usage = Label(ram_information_window, text="RAM usage: ", font=("Courier", 15))
    label_ram_usage.grid(row=5, sticky=E)

    # === Call Functions === #
    drop_down_menu(ram_information_window)
    draw_ram_percent()
    draw_ram_total_used_free()

    ram_information_window.mainloop()


# === Draw Extended Disk Info === #
def draw_extended_disk_information():
    disk_information_window = Tk()
    disk_information_window.title("Disk Information")

    def draw_disk_total_used_free_percent():
        disk_usage = psutil.disk_usage(path="C:\\")
        total_disk_usage = disk_usage.total / (2 ** 30)
        used_disk_usage = disk_usage.used / (2 ** 30)
        free_disk_usage = disk_usage.free / (2 ** 30)

        try:
            # === Total Disk Space === #
            label_total_disk2 = Label(disk_information_window, text=str(round(total_disk_usage, 1)) + " GB",
                                      font=("Courier", 15), width=10)
            label_total_disk2.grid(row=2, column=2)

            # === Used Disk Space === #
            label_used_disk2 = Label(disk_information_window, text=str(round(used_disk_usage, 1)) + " GB",
                                     font=("Courier", 15), width=10)
            label_used_disk2.grid(row=3, column=2)

            # === Free Disk Space === #
            label_free_disk2 = Label(disk_information_window, text=str(round(free_disk_usage, 1)) + " GB",
                                     font=("Courier", 15), width=10)
            label_free_disk2.grid(row=4, column=2)

            # === Disk Space Percent === #
            label_disk_usage_perf = Label(disk_information_window, text=str(round(disk_usage.percent, 1)) + "%",
                                          font=("Courier", 15), width=5)
            label_disk_usage_perf.grid(row=5, column=2)

            threading.Timer(1, draw_disk_total_used_free_percent).start()
        except Exception as e:
            print(e)

    # === Labels === #
    label_extended_disk_title = Label(disk_information_window, text="Disk Information", font=("Courier", 25))
    label_extended_disk_title.grid(row=1, columnspan=15)

    label_total_disk1 = Label(disk_information_window, text="Total Disk Space: ", font=("Courier", 15))
    label_total_disk1.grid(row=2, sticky=E)
    label_used_disk1 = Label(disk_information_window, text="Used Disk Space: ", font=("Courier", 15))
    label_used_disk1.grid(row=3, sticky=E)
    label_free_disk1 = Label(disk_information_window, text="Free Disk Space: ", font=("Courier", 15))
    label_free_disk1.grid(row=4, sticky=E)
    label_disk_usage = Label(disk_information_window, text="Disk Usage: ", font=("Courier", 15))
    label_disk_usage.grid(row=5, sticky=E)

    # === Call Functions === #
    drop_down_menu(disk_information_window)
    draw_disk_total_used_free_percent()

    disk_information_window.mainloop()


draw_system_information()
