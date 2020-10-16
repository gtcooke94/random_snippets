from collections import UserString
from collections.abc import MutableSequence
from contextlib import contextmanager
from contextlib import wraps


from collections import UserList


class MutableString(UserList, str):
    def __init__(self, string):
        self.data = list(string)

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

    # this could be inside or outside of the class. Remember self.<method> makes self the first argument, so this doesn't have that based on the way we are calling it
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


# Inspired by solutions:
class MutableStringSoln(MutableSequence, UserString, str):
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
