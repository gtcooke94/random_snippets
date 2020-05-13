Original solutions at the bottom for reference.

Improvements:
No need to use `metaclass=abc.ABCMeta`. This can directly inherit from `ABC`.

```
- class Validator(metaclass=abc.ABCMeta):
+ class Validator(abc.ABC):
```

We can use `__set_name__` to know the name of our descriptor. Then we can assign the value directly on the object, rather than keeping a `self.data` on the descriptor!

`__set_name__(self, owner, name)` Gets called when the descriptor is created like follows
```
class Thing:
    x = PositiveNumber(1)
```
Gets called as `__set_name__(self, <Thing instance>, "x")`


Can be done as such: I like this better because you don't have to worry about the `WeakKeyDictionary`. And we get to store the value on the actual object, which I really like.

```
class Validator(abc.ABC):
    def __init__(self, default=NOT_SET):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, obj_type):
        try:
            value = getattr(obj, self.name)
        except AttributeError:
            if self.default is NOT_SET:
                raise AttributeError
            value = self.default
        return value

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.name, value)

    @abc.abstractmethod
    def validate(self, value):
        pass


class PositiveNumber(Validator):
    def validate(self, value):
        if value <= 0:
            raise ValueError()
```




Original Solutions:
```

from weakref import WeakKeyDictionary
import abc

NOT_SET = object()


class Validator(metaclass=abc.ABCMeta):
    def __init__(self, default=NOT_SET):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, obj, obj_type):
        value = self.data.get(obj, self.default)
        if value is NOT_SET:
            raise AttributeError
        return value

    def __set__(self, obj, value):
        self.validate(value)
        self.data[obj] = value

    @abc.abstractmethod
    def validate(self, value):
        pass


class PositiveNumber(Validator):
    def validate(self, value):
        if value <= 0:
            raise ValueError()


# Through bonus 1
#  class PositiveNumber:
#      def __init__(self, default=NOT_SET):
#          self.default = default
#          self.data = WeakKeyDictionary()
#
#      def __get__(self, obj, obj_type):
#          value = self.data.get(obj, self.default)
#          if value is NOT_SET:
#              raise AttributeError
#          return value
#
#      def __set__(self, obj, value):
#          if value <= 0:
#              raise ValueError()
#          self.data[obj] = value
#
#
```
