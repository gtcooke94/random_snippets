import csv


def row_factory(fields):
    """Return a memory-efficient Row classwhich accepts specific fields."""
    class Row:
        __slots__ = fields
        def __init__(self, *args, **kwargs):
            for name, arg in zip(self.__slots__, args):
                setattr(self, name, arg)
            for key in kwargs:
                setattr(self, key, kwargs[key])
        def __iter__(self):
            for key in self.__slots__:
                yield getattr(self, key)
        def __repr__(self):
            attrs = (
                f"{name}={getattr(self, name)!r}"
                for name in self.__slots__
            )
            return f"{type(self).__name__}({', '.join(attrs)})"
    return Row


class FancyReader:

    """Sort of like a memory-effecient version of DictReader."""

    def __init__(self, iterable, *, fieldnames=None, **kwargs):
        self.reader = csv.reader(iterable, **kwargs)
        self.fieldnames = fieldnames
        self.line_num = 0
        self.Row = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.Row is None:
            self.Row = row_factory(self.fieldnames)
        row = self.Row(*next(self.reader))
        self.line_num += 1
        return row

    @property
    def fieldnames(self):
        if self._fieldnames is None:
            self._fieldnames = next(self.reader)
            self.line_num += 1
        return self._fieldnames

    @fieldnames.setter
    def fieldnames(self, fieldnames):
        self._fieldnames = fieldnames
