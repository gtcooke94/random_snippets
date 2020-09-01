"""
Refactoring some. I don't like a few things:
    1. ErrorOverrideDict is too specific to the usecase of MetaNoMethodCollision. Responsibilities are mixed
    2. Our error doesn't tell us what was overriden
    3. It feels weird just have a `pass` in `NoMethodCollisions`
"""
from collections import UserDict


class OverrideTrackingDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.overridden = set()
        super().__init__(*args, **kwargs)

    def __setitem__(self, name, val):
        if name in self.data:
            self.overridden.add(name)
        self.data[name] = val


class MetaNoMethodCollisions(type):
    """The __prepare__ method must return a mapping that you want to use for your classes namespace.
    Each item in the namespace will be added to this mapping
    """

    @classmethod
    def __prepare__(metacls, name, bases):
        return OverrideTrackingDict()

    def __new__(cls, name, bases, namespace):
        for attr in namespace.overridden:
            value = namespace[attr]
            if type(value) != property and (
                callable(value) or hasattr(value, "__get__")
            ):
                raise TypeError(
                    f"Method collision. {attr} defined multiple times in {name}"
                )
        # Need to convert from UserDict to dict, because this _requires_ a dict.
        return super().__new__(cls, name, bases, dict(namespace))


class NoMethodCollisions(metaclass=MetaNoMethodCollisions):
    """Disallows class atrributes to be redefined."""

    pass


# First solution to all 3
'''
from collections import UserDict

class ErrorOverrideDict(UserDict):
    def __setitem__(self, name, val):
        if (name in self.data and type(val) != property and (callable(val) or hasattr(val, "__get__"))):
            raise TypeError("Method collision")
        self.data[name] = val


class MetaNoMethodCollisions(type):
    """The __prepare__ method must return a mapping that you want to use for your classes namespace.
    Each item in the namespace will be added to this mapping
    """
    @classmethod
    def __prepare__(metacls, name, bases):
        return ErrorOverrideDict()

    def __new__(cls, name, bases, namespace):
        """Need to convert from UserDict to dict, because this _requires_ a dict."""
        return super().__new__(cls, name, bases, dict(namespace))

class NoMethodCollisions(metaclass=MetaNoMethodCollisions):
    pass
'''
