The base question and first two bonuses came very easily from my previous `FancyReader` implementation.
Bonus 3 required a large change. I realized that I was going to have to construct different classes on the fly for Bonus 3. With the problem saying it might be very difficult, I realized that I'd likely have to reach for `metaclasses`, something with which I am not terribly familiar. However, I ended up getting a working answer:

```
from csv import reader


class FancyReader:
    def __init__(self, lines, fieldnames=None, delimiter=","):
        self.line_num = 0
        self.lines = reader(lines, delimiter=delimiter)
        self._fieldnames = fieldnames

    def __iter__(self):
        return self

    def __next__(self):
        self.line_num += 1
        return self.make_row(self.fieldnames, next(self.lines))

    def make_row(self, fieldnames, values):
        class Row(metaclass=RowMeta, fieldnames=self.fieldnames):
            def __init__(self, fieldnames, values):
                for fieldname, value in zip(fieldnames, values):
                    setattr(self, fieldname, value)

            def __repr__(self):
                inside = ", ".join(
                    f"{fieldname}={repr(getattr(self, fieldname))}"
                    for fieldname in self.__slots__
                )
                return f"Row({inside})"

            def __iter__(self):
                yield from (getattr(self, field) for field in self.__slots__)

        return Row(fieldnames, values)

    @property
    def fieldnames(self):
        if not self._fieldnames:
            self.line_num += 1
            self._fieldnames = next(self.lines)
        return self._fieldnames


class RowMeta(type):
    def __new__(cls, name, bases, dctn, **kwargs):
        dctn["__slots__"] = [str(i) for i in kwargs["fieldnames"]]
        return type.__new__(cls, name, bases, dctn)
```

`RowMeta` is a metaclass that takes `fieldnames` as a keyword argument, and makes sure it constructs classes that have those fieldnames as slots. The `__new__` for a metaclass is called on the creation of a new class, so the fieldnames have to be specified in the class definition, which felt very weird to me, because usually I'm just doing inheritance there.
I tried to put methods on `RowMeta` that I wanted `Row` to inherit, but that doesn't work. The `Row` class itself inherits them, not _instances_ of the `Row` class.
My implmentation is thus to have a `make_row` function that creates an instance of `Row`, which has a metaclass of `RowMeta`. This yields similar syntax to using the `NamedTuple` approach that I used prior to bonus 3.
I had to mess around a lot with the order in which __new__, __init__, etc are all called in construction of my `Row` class, but this ended up working, and doesn't seem too terrible.
