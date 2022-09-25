import logging
import pyfiglet
import threading
import sys
import time
import os

from classes.FileMonInstance import FileMonInstance
from classes.FileMonInstance import stop_event

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
instances = []


def start():
    clear, back_slash = "clear", "/"
    if os.name == "nt":
        clear, back_slash = "cls", "\\"

    os.system(clear)
    sys.stdout.flush()
    print(pyfiglet.figlet_format(f"FileMon") + "\n-----------------------------------")


paths = [
    "path/to/file",
]


if __name__ == "__main__":
    start()
    for path in paths:
        fileMonInstance = FileMonInstance(path)
        instance_thread = threading.Thread(target=fileMonInstance.run)
        instance_thread.daemon = True

        instances.append(instance_thread)

        instance_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info(f"User stopped observers!")
        stop_event.set()
        for instance in instances:
            instance.join()
        sys.exit()
