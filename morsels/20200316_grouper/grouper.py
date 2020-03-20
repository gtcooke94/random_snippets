from collections import UserDict
from collections import defaultdict


class Grouper(UserDict):
    def __init__(self, iterable=None, key=None):
        super().__init__()
        self.data = defaultdict(list)
        self.key = key
        if iterable:
            self.group(iterable)

    def group(self, iterable):
        if isinstance(iterable, dict):
            self.group_from_dict(iterable)
            return
        for item in iterable:
            self.add(item)

    def group_from_dict(self, d):
        for key, value in d.items():
            self.data[key].extend(value)

    def update(self, iterable):
        self.group(iterable)

    def add(self, item):
        group = self.key(item)
        self.data[group].append(item)

    def group_for(self, item):
        return self.key(item)

    def __add__(self, other):
        if not self.key == other.key:
            raise ValueError("Key functions not the same, cannot add Groupers together")
        new_grouper = Grouper(dict(self))
        new_grouper.update(dict(other))
        return new_grouper
