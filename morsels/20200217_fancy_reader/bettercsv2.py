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
