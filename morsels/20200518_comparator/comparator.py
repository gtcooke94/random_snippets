from numbers import Number
from contextlib import contextmanager


class Comparator:

    default_delta_value = 0.0000001

    def __init__(self, value, delta=None):
        if delta is None:
            self.delta = Comparator.default_delta_value
        else:
            self.delta = delta
        self.value = value

    def __eq__(self, other_value):
        # Could use math.isclose as well
        return other_value - self.delta <= self.value <= other_value + self.delta

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, delta={self.delta})"

    def __add__(self, other):
        if isinstance(other, Number):
            return Comparator(self.value + other, delta=self.delta)
        elif isinstance(other, Comparator):
            return Comparator(
                self.value + other.value, delta=max(self.delta, other.delta)
            )
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Number):
            return Comparator(self.value - other, delta=self.delta)
        elif isinstance(other, Comparator):
            return Comparator(
                self.value - other.value, delta=max(self.delta, other.delta)
            )
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Number):
            return Comparator(other - self.value, delta=self.delta)
        elif isinstance(other, Comparator):
            return Comparator(
                other.value - self.value, delta=max(self.delta, other.delta)
            )
        return NotImplemented

    # I think it is more correct to have this as a class method
    @classmethod
    @contextmanager
    def default_delta(cls, delta):
        old_default_delta = cls.default_delta_value
        try:
            cls.default_delta_value = delta
            yield
        finally:
            cls.default_delta_value = old_default_delta

    # Solution:
    #  @contextmanager
    #  def default_delta(delta):
    #      old_default_delta = Comparator.default_delta_value
    #      try:
    #          Comparator.default_delta_value = delta
    #          yield
    #      finally:
    #          Comparator.default_delta_value = old_default_delta
