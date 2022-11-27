from time import sleep, time

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.is_running = False
        self.args = args
        self.kwargs = kwargs
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        start = int(time() * 1000)
        i = 0
        if not self.is_running:
            self.is_running = True

            while True:
                if not self.is_running:
                    break

                i += 1
                now = int(time() * 1000)
                sleep_ms = i * self.interval - (now - start)
                if sleep_ms < 0:
                    self.function(*self.args, **self.kwargs)
                else:
                    sleep(sleep_ms / 1000.0)
                    self.function(*self.args, **self.kwargs)

    def stop(self):
        self.is_running = False
# def hello(name):
#     print(f"[{time()}]\t Hello {name}!")
#     sleep(0.01)


# print("starting...")

# rt = RepeatedTimer(1, hello, "world")
# try:
#     sleep(50)
# finally:
#     rt.stop()
