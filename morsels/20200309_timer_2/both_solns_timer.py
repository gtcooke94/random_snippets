import time
from contextlib import ContextDecorator
from statistics import mean, median


class Timer(ContextDecorator):
    name_instance_mapping = dict()

    def __new__(cls, *args, **kwargs):
        #  import pdb; pdb.set_trace()
        if len(args) == 1:
            name = args[0]
            if name in cls.name_instance_mapping:
                return cls.name_instance_mapping[name]
            else:
                instance = super().__new__(cls)
                cls.name_instance_mapping[name] = instance
                return instance
        else:
            return super().__new__(cls)


    def __init__(self, name=None, *, func=None, parent=None):
        self.runs = []
        self.func = func
        self.split_timers = []
        self.split_names = []
        self.parent = parent
        self.in_use = False

    def __enter__(self):
        if self.parent and not self.parent.in_use:
            raise RuntimeError("Cannot split because parent timer is not running")
        self.in_use = True
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.time() - self.start
        self.runs.append(self.elapsed)
        self.in_use = False
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

    def __getitem__(self, identifier):
        if isinstance(identifier, int):
            return self.split_timers[identifier]
        else:
            return self.split_timers[self.split_names.index(identifier)]

    def split(self, name=None):
        if name and name in self.split_names:
            return self.__getitem__(name)

        self.split_names.append(name)
        self.split_timers.append(Timer(parent=self))
        return self.split_timers[-1]

