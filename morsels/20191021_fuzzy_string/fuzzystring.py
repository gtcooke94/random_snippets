import unicodedata


class FuzzyString:
    def __init__(self, string):
        self.string = string

    def _normalize_string(self, o):
        return unicodedata.normalize("NFD", o.upper().lower())

    def __eq__(self, o):
        if isinstance(o, str):
            return self._normalize_string(self.string) == self._normalize_string(o)

    def __gt__(self, o):
        return self._normalize_string(self.string) > self._normalize_string(o)

    def __lt__(self, o):
        return self._normalize_string(self.string) < self._normalize_string(o)

    def __le__(self, o):
        return self._normalize_string(self.string) <= self._normalize_string(o)

    def __ge__(self, o):
        return self._normalize_string(self.string) >= self._normalize_string(o)

    def __ne__(self, o):
        return not self == o

    def __str__(self):
        return self.string

    def __repr__(self):
        return repr(self.string)

    def __contains__(self, item):
        return item.lower() in self._normalize_string(self.string)

    def __add__(self, o):
        return FuzzyString(self.string + o)

'''
from functools import total_ordering
@totalordering is a decorator. Decorate FuzzyString, and by just implementing __eq__ and __lt__, you get all of the others for free

Also should use string.casefold() instead of string.lower() or string.upper(). It's a unicode aware case operator.

Final good solution from Morsels:
Ordered is an Abstract Base Class, we say that it has @total_ordering, but then use it as an interface in our actual class. That class must then implement __lt__ and __eq__, and will have the requisite total ordering (even though in this case UserString has it's own, because we inherit from Ordered first, it overrides the operators in UserString). Then uses the same normalize I found, to the decomposed form, but uses casefold as its the right thing to use vs. upper() and lower() when dealing with unicode

from abc import ABC, abstractmethod
from functools import total_ordering
from collections import UserString
import unicodedata

def normalize(string):
    return unicodedata.normalize("NFD", string.casefold())


@total_ordering
class Ordered(ABC):
    """Mixin class which defines <=, >, >= based on < and ==."""
    @abstractmethod
    def __lt__(self, other):
        """Child class must implement __lt__."""
    @abstractmethod
    def __eq__(self, other):
        """Child class must implement __eq__."""


class FuzzyString(Ordered, UserString):
    def __lt__(self, other):
        return normalize(self.data) < normalize(other)
    def __eq__(self, other):
        return normalize(self.data) == normalize(other)
    def __contains__(self, substring):
        return normalize(substring) in normalize(self.data)
'''
