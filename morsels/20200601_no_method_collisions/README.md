Had to look up hints/solution for this one, had never looked at `__prepare__` before

My understanding is this:
On class creation, will check metaclass. The `__prepare__` is one of the first things to get run. It must return a Mapping. This mapping is what is used to setup the classes namespace, so essentially as Python reads the code for you class, say this one:

```
class SillyTests(NoMethodCollisions):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
    def test_subtract(self):
        self.assertEqual(4 - 2, 2)
    def test_add(self):
        self.assertEqual(1 + 1, 2)
```

The `__prepare__` will return a Mapping object that will get it's `__set_item__` called with the following args:
```
>>> from classtools import NoMethodCollisions
__module__ classtools
__qualname__ NoMethodCollisions
>>> class SillyTests(NoMethodCollisions):
...     def test_add(self):
...         self.assertEqual(2 + 2, 4)
...     def test_subtract(self):
...         self.assertEqual(4 - 2, 2)
...     def test_add(self):
...         self.assertEqual(1 + 1, 2)
...
__module__ __main__
__qualname__ SillyTests
test_add <function SillyTests.test_add at 0x105490b80>
test_subtract <function SillyTests.test_subtract at 0x105537790>
test_add <function SillyTests.test_add at 0x105537820>
```


# Core Solution + Bonus 1 (Bonus 1 was just make the error a TypeError)
Have a dict that doesn't allow Overriding

```
from collections import UserDict

class ErrorOverrideDict(UserDict):
    def __setitem__(self, name, val):
        print(name, val)
        if name in self.data:
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

```

# Bonus 2
Allow properties
Just replace `if name in self.data` with `if name in self.data and type(val) != property`
Properties are descriptors and it's okay for this to happen

# Bonus 3
Only check for method collisions on callables and descriptors (like `classmethod` and `staticmethod`)

Only checking on callables is easy, just add `if callable(val)` in the `if` statement

Not sure how to check for the `classmethod` and `staticmethod`
Interestingly, this solution causes the `test_non_functions` test to break
```
from collections import UserDict

class ErrorOverrideDict(UserDict):
    def __setitem__(self, name, val):
        if (name in self.data and type(val) != property and callable(val)):
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
```


Having to look at solutions for inspiration
Turns out, we need to get for `__get__` to see if it is a descriptor. But we have to be careful about the property check as well from Bonus 2

The following passes everything:
```
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
```


Did some refactoring for the following reasons:
    1. ErrorOverrideDict is too specific to the usecase of MetaNoMethodCollision. Responsibilities are mixed
    2. Our error doesn't tell us what was overriden
    3. It feels weird just have a `pass` in `NoMethodCollisions` - I don't think I can get around this


Final solution is here:
```
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
```
