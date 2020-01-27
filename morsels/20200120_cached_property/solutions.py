"""
Here's a fully working solution that uses the random attribute name approach:
"""

from uuid import uuid4


class cached_property:
    def __init__(self, func):
        self._getter = func
        self._setter = self._deleter = None
        self.attr = 'property_' + uuid4().hex
    def __get__(self, obj, obj_type):
        if obj is None:
            return self
        if not hasattr(obj, self.attr):
            setattr(obj, self.attr, self._getter(obj))
        return getattr(obj, self.attr)
    def __set__(self, obj, value):
        if self._setter:
            self._setter(obj, value)
            delattr(obj, self.attr)
        else:
            setattr(obj, self.attr, value)
    def __delete__(self, obj):
        delattr(obj, self.attr)
        if self._deleter:
            self._deleter(obj)
    def setter(self, setter):
        self._setter = setter
        return self
    def deleter(self, deleter):
        self._deleter = deleter
        return self
"""
In our __set__, if we have a setter method, we call it and then clear our cached value. Otherwise we overwrite our cached value as before.

In our __delete__, we clear our cached value and then call our deleter method (if we have one).

My favorite solution uses relies on Python 3.6's __set_name__ to set the correct attribute name on the object directly:
"""

class cached_property:
    def __init__(self, func):
        self._getter = func
        self._setter = self._deleter = None
        self.name = None
    def setter(self, setter):
        self._setter = setter
        return self
    def deleter(self, deleter):
        self._deleter = deleter
        return self
    def __get__(self, obj, obj_type):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            value = obj.__dict__[self.name]
        else:
            value = self._getter(obj)
        obj.__dict__[self.name] = value
        return value
    def __set__(self, obj, value):
        if self._setter:
            self._setter(obj, value)
            obj.__dict__.pop(self.name, None)
        else:
            obj.__dict__[self.name] = value
    def __delete__(self, obj):
        obj.__dict__.pop(self.name, None)
        if self._deleter:
            self._deleter(obj)
    def __set_name__(self, obj, name):
        self.name = name
"""
Note that we need to write to (and read from) obj.__dict__ directly here because if we used setattr we'd end up with a recursion error (since setting the correct attribute name will result in our descriptors' __set__ being called which will then call setattr again and so on.
"""
