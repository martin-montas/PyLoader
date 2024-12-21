import threading
import pdb


class StoppableThread(threading.Thread):
    def __init__(self, target=None, args=()):
        super().__init__()
        self.daemon = True
        self.target = target
        self.args = args
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            if self.target:
                self.target(*self.args)

    def stop(self):
        pdb.set_trace()
        self._stop_event.set()
        print("stopping the thread")




# Example usage
# thread = StoppableThread()
# thread.start()
# time.sleep(5)
# thread.stop()
# thread.join()
# print("Thread has been stopped.")
