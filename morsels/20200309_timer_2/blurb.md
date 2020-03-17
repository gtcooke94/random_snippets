First go at a full solution. I'm going to refactor a bit, but this does work:
```
import time


class Timer:
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
```

After looking at the provided solution, there are a few things I can make better.
1. There is no need for `self.parent`. The check for `in_use` can (and should) happen in `split()` rather than in the `__enter__` of the sub-timer.
2. I keep two lists and deal with getting indices between them. Sure feels a lot like a dictionary.
3. time.perf_counter() is better for this use case than time.now()
4. I have extra args in my timer that then don't need to be used, so I can clean up `__new__` and `__init__`


Refactored version, with an alternative `split` implementation using `dictionary.setdefault` as well
```
import time


class Timer:
    name_instance_mapping = dict()

    def __new__(cls, name=None):
        if not name:
            return super().__new__(cls)
        if name in cls.name_instance_mapping:
            return cls.name_instance_mapping[name]
        instance = super().__new__(cls)
        cls.name_instance_mapping[name] = instance
        return instance

    def __init__(self, name=None):
        # We could be re-initting an already created object because of named timers.
        # We don't want to reset all the attributes if that is the case
        if not hasattr(self, "in_use"):
            self.runs = []
            self.unnamed_splits = []
            self.named_splits = {}
            self.in_use = False
            self.name = name

    def __enter__(self):
        self.in_use = True
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        self.runs.append(self.elapsed)
        self.in_use = False
        return False

    def __getitem__(self, identifier):
        if isinstance(identifier, int):
            return self.unnamed_splits[identifier]
        else:
            return self.named_splits[identifier]

    def split(self, name=None):
        if not self.in_use:
            raise RuntimeError("Timer but be in-use to be split")
        if name:
            if name in self.named_splits:
                return self.__getitem__(name)
            else:
                self.named_splits[name] = Timer()
                return self.__getitem__(name)

        self.unnamed_splits.append(Timer())
        return self.unnamed_splits[-1]

    """
    Alternative implementation with `setdefault`, which does the following:
    dictionary.setdefault(key, value)
    1. If the key is in the dict, return the value for that key
    2. If the key is not in the dict, set dictionary[key] = value and return value

    def split(self, name=None):
        if not self.in_use:
            raise RuntimeError("Timer but be in-use to be split")
        if name:
            return self.named_splits.setdefault(name, Timer())
        self.unnamed_splits.append(Timer())
        return self.unnamed_splits[-1]
    """
```
