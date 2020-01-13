import time
from contextlib import ContextDecorator
from statistics import mean, median


class Timer(ContextDecorator):
    def __init__(self, func=None):
        self.runs = []
        self.func = func

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.time() - self.start
        self.runs.append(self.elapsed)
        return False

    def __call__(self, *args, **kwargs):
        with self:
            ret = self.func(*args, **kwargs)
        return ret



    @property
    def mean(self):
        return mean(self.runs)

    @property
    def median(self):
        return median(self.runs)

    @property
    def max(self):
        return max(self.runs)

    @property
    def min(self):
        return min(self.runs)
