import time
import logging
import threading
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

stop_event = threading.Event()


class FileMonInstance:
    def __init__(self, path_to_monitor: str):
        self.observer = Observer()
        self.event_handler = LoggingEventHandler()
        self.path_to_monitor = path_to_monitor
        self.running = True

    def run(self):
        try:
            self.observer.schedule(
                self.event_handler, self.path_to_monitor, recursive=True
            )
            self.observer.start()
            logging.info(f"Observer on path: {self.path_to_monitor} started!")
        except WindowsError as e:
            self.running = False
            if e.winerror == 2:
                logging.error(
                    f"Something went wrong while trying to start the observer on path: {self.path_to_monitor}! The file does not exist!"
                )
        except Exception as e:
            self.running = False
            logging.error(
                f"Something went wrong while trying to start the observer on path: {self.path_to_monitor}! Got error: {e}!"
            )

        if self.running:
            try:
                while not stop_event.is_set():
                    time.sleep(1)
            except Exception as e:
                self.observer.stop()
                logging.error(
                    f"Stopped observer on path: {self.path_to_monitor} with error: {e}!"
                )

            self.observer.stop()
            self.observer.join()
