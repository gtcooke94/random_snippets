Idea: If we want a string to be mutable, we need to represent it with a mutable sequence, so we'll use a list
The following solves the base questions as well as bonus 1

The `__getitem__` is slightly strange, because if it's a slice it already returns a MutableString, whereas if it's a single index it returns a normal string. This is because the `super.__getitem__()` calls `self.__class__(self.data[i])`, which of course returns a `MutableString` because `self.__class__()` constructs a `MutableString`.

```
from collections import UserList


class MutableString(UserList):
    def __init__(self, string):
        self.data = list(string)

    def stringify(self):
        return "".join(self.data)

    def __eq__(self, other):
        if isinstance(other, MutableString):
            return self.data == other.data
        elif isinstance(other, str):
            return str(self) == other

    def __str__(self):
        return "".join(self.data)

    def __repr__(self):
        return repr(str(self))

    def pop(self, *args):
        return MutableString(super().pop(*args))

    def __getitem__(self, *args):
        ret = super().__getitem__(*args)
        if isinstance(ret, MutableString):
            return ret
        return MutableString(ret)
```

For bonus 2, we needed regular string methods to work. I just delegated the ones in the test to `str(self)`. I wonder if there's a better way to do this:
The following were added
```
    def replace(self, *args, **kwargs):
        return MutableString(str(self).replace(*args, **kwargs))

    def upper(self, *args, **kwargs):
        return MutableString(str(self).upper(*args, **kwargs))

    def lower(self, *args, **kwargs):
        return MutableString(str(self).lower(*args, **kwargs))

    def endswith(self, *args, **kwargs):
        return str(self).endswith(*args, **kwargs)
```

Bonus 3 was simply solved by inheriting from `str` _after_ `UserList` in the chain
This way it'll still be seen as a string, but the `UserList` methods take precedence

Solution passing all the tests:

```
from collections import UserList


class MutableString(UserList, str):
    def __init__(self, string):
        self.data = list(string)

    def stringify(self):
        return "".join(self.data)

    def __eq__(self, other):
        if isinstance(other, MutableString):
            return self.data == other.data
        elif isinstance(other, str):
            return str(self) == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "".join(self.data)

    def __repr__(self):
        return repr(str(self))

    def pop(self, *args):
        return MutableString(super().pop(*args))

    def __getitem__(self, *args):
        ret = super().__getitem__(*args)
        if isinstance(ret, MutableString):
            return ret
        return MutableString(ret)

    def replace(self, *args, **kwargs):
        return MutableString(str(self).replace(*args, **kwargs))

    def upper(self, *args, **kwargs):
        return MutableString(str(self).upper(*args, **kwargs))

    def lower(self, *args, **kwargs):
        return MutableString(str(self).lower(*args, **kwargs))

    def endswith(self, *args, **kwargs):
        return str(self).endswith(*args, **kwargs)
```

Here is a way to replace the repetitive string function calls:

```
    def _proxy(methodname):
        @wraps(methodname)
        def string_function_wrapper(self, *args, **kwargs):
            ret = getattr(str(self), methodname)(*args, **kwargs)
            return MutableString(ret) if isinstance(ret, str) else ret
        return string_function_wrapper

    replace = _proxy("replace")
    upper = _proxy("upper")
    lower = _proxy("lower")
    endswith = _proxy("endswith")
```

Inspired by the solutions, I also wrote this. It's shorter and uses the multiple inheritance between MutableSequence and UserString. Then `str` just allows this to be used anywhere a string is used.
```
class MutableString(MutableSequence, UserString, str):
    @contextmanager
    def chars(self):
        chars = list(self.data)
        yield chars
        self.data = "".join(str(c) for c in chars)

    def __delitem__(self, i):
        with self.chars() as chars:
            del chars[i]

    def __setitem__(self, i, val):
        with self.chars() as chars:
            chars[i] = val

    def insert(self, i, val):
        with self.chars() as chars:
            chars.insert(i, val)

    def __imul__(self, scalar):
        with self.chars() as chars:
            chars *= scalar
        return self

    def __ne__(self, other):
        return not self == other
```
