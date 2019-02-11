import time

# Decorator based timer
from contextlib import contextmanager

@contextmanager
def timeblock():
    try:
        start_time = time.time()
        yield start_time
    finally:
        end_time = time.time()
        print("Time elapsed for context manager implementation {}".format(end_time - start_time))

# Class based timer
class TimeBlock():
    elapsed_time = 0
    start_time = 0

    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        print("Time Elapsed {}".format(self.elapsed_time))


class Indenter:
    level = 0
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level = self.level + 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level = self.level - 1

    def pprint(self, str):
        print("    " * self.level + str)


if __name__ == "__main__":
    print("Starting")
    with TimeBlock() as timer:
        time.sleep(2)
        with Indenter() as ind: 
            ind.pprint("First")
            ind.pprint("First")
            with ind:
                ind.pprint("Second")
                ind.pprint("Second")
            ind.pprint("First")
            ind.pprint("First")
            ind.pprint("First")
            with ind:
                ind.pprint("Second")
                ind.pprint("Second")
                with ind:
                    ind.pprint("Third")
                    ind.pprint("Third")
                    ind.pprint("Third")
                ind.pprint("Second")
                ind.pprint("Second")
                ind.pprint("Second")
            ind.pprint("First")
            ind.pprint("First")
    print("Done")
    with timeblock() as timer:
        time.sleep(2)
        with Indenter() as ind: 
            ind.pprint("First")
            ind.pprint("First")
            with ind:
                ind.pprint("Second")
                ind.pprint("Second")
            ind.pprint("First")
            ind.pprint("First")
            ind.pprint("First")
            with ind:
                ind.pprint("Second")
                ind.pprint("Second")
                with ind:
                    ind.pprint("Third")
                    ind.pprint("Third")
                    ind.pprint("Third")
                ind.pprint("Second")
                ind.pprint("Second")
                ind.pprint("Second")
            ind.pprint("First")
            ind.pprint("First")
