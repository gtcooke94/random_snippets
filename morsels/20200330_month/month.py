from functools import total_ordering
from datetime import date
from calendar import monthrange
from dataclasses import dataclass

# Using dataclass lets you lose the init, has, setattr, and delattr methods
@dataclass(frozen=True)
@total_ordering
class Month:
    __slots__ = ["year", "month", "first_day", "last_day"]
    year: int
    month: int

    def __post_init__(self):
        super().__setattr__("first_day", date(self.year, self.month, 1))
        super().__setattr__(
            "last_day",
            date(self.year, self.month, monthrange(self.year, self.month)[1]),
        )

    @classmethod
    def from_date(cls, date):
        return cls(date.year, date.month)

    def strftime(self, fmt):
        return self.first_day.strftime(fmt)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month:02d}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        if isinstance(other, date):
            return False
        return False

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, -self.month) < (other.year, -other.month)
        raise TypeError()


#  No dataclass implementation
@total_ordering
class Month2:
    __slots__ = ["year", "month", "first_day", "last_day"]

    def __init__(self, year, month):
        super().__setattr__("year", year)
        super().__setattr__("month", month)
        super().__setattr__("first_day", date(year, month, 1))
        super().__setattr__("last_day", date(year, month, monthrange(year, month)[1]))

    @classmethod
    def from_date(cls, date):
        return cls(date.year, date.month)

    def strftime(self, fmt):
        return self.first_day.strftime(fmt)

    def __setattr__(self, attr, value):
        raise Exception()

    def __delattr__(self, attr):
        raise Exception()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month:02d}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        if isinstance(other, date):
            return False
        return False

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, -self.month) < (other.year, -other.month)
        raise TypeError()

    def __hash__(self):
        return hash(str(self))
