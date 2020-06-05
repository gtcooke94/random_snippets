from datetime import date
from calendar import monthrange
from dataclasses import dataclass
from functools import total_ordering
import math
import operator

MONTHS_PER_YEAR = 12


@dataclass(frozen=True, order=True)
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

    def __sub__(self, other):
        """ Month's don't know how to subtract MonthDeltas to themselves, raise
        NotImplemented to get MonthDelta's __radd__
        
        Months only know how to subtract themselves to get monthdeltas
        """
        if not isinstance(other, Month):
            return NotImplemented
        year_diff = self.year - other.year
        month_diff = self.month - other.month
        return MonthDelta(year_diff * MONTHS_PER_YEAR + month_diff)

    __format__ = strftime


@dataclass(frozen=True)
class MonthDelta:
    __slots__ = ["months"]
    months: int

    def __add__(self, other):
        if isinstance(other, Month):
            return self.combine_with_month(other, operator.add)
        elif isinstance(other, MonthDelta):
            return MonthDelta(self.months + other.months)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, MonthDelta):
            return MonthDelta(self.months - other.months)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Month):
            return self.combine_with_month(other, operator.add)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Month):
            return self.combine_with_month(other, operator.sub)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.mult(other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months / other)
        elif isinstance(other, MonthDelta):
            return self.months / other.months
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months // other)
        elif isinstance(other, MonthDelta):
            return self.months // other.months
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months % other)
        elif isinstance(other, MonthDelta):
            return self.months % other.months
        return NotImplemented

    def __neg__(self):
        return MonthDelta(-self.months)

    def mult(self, other):
        return MonthDelta(self.months * other)

    def combine_with_month(self, month, operation):
        month_combination = operation(month.month, self.months)
        years_change = month_combination // MONTHS_PER_YEAR
        leftover_months = month_combination - (years_change * MONTHS_PER_YEAR)
        if leftover_months > 0:
            result_month = leftover_months
        elif leftover_months < 0:
            result_month = 12 + leftover_months
        else:
            # not elegant, but weird case doing calculation this way if month_change is a multiple of -12
            if years_change < 0:
                result_month = 12 + leftover_months
                years_change -= 1
            if years_change >= 0:
                result_month = month.month

        result_year = month.year + years_change
        return Month(result_year, result_month)
