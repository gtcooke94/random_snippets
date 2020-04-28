This one is very interesting. Had to go looking at the solution for hints.

The initial thought of raising `TypeError` in `__init__` doesn't work, because subclasses don't have to call `__init__`. However, I think that subclasses should always chain calls to `super().__new__()`, because eventually they need to get constructed. That leads to this solution.

```
class Unsubclassable:
    def __new__(cls, *args, **kwargs):
        if cls is not Unsubclassable:
            raise TypeError("Trying to subclass Unsubclassable")
        return super().__new__(cls, *args, **kwargs)
```

Bonus 1 wants us to do it at the time the class is declared, not on creation. We have to reach into `metaclasses` here, because `__new__` will of course only do it on initialization. Originally I wanted to check if `Unsubclassable in bases`, but that doesn't work because it isn't defined yet. However, `Unsubclassable` can't have ANY bases.

```
class UnsubclassableType(type):
    def __new__(cls, name, bases, dctn, **kwargs):
        if bases != ():
            raise TypeError("Trying to subclass Unsubclassable")
        return super().__new__(cls, name, bases, dctn)

class Unsubclassable(metaclass=UnsubclassableType):
    pass
```

Even better... `__init_subclass__` of class A is called if class B is a subclass of class A
```
class Unsubclassable():
    def __init_subclass__(cls):
        raise TypeError("Trying to subclass Unsubclassable")
```

Bonus 2: Knowing about `__init_subclass__` makes this really easy. Give it the above method

```
class Unsubclassable():
    def __init_subclass__(cls):
        raise TypeError("Trying to subclass Unsubclassable")


def final_class(cls):
    cls.__init_subclass__ = lambda x: TypeError()
    return cls
```

Even better:

```
def final_class(cls):
    cls.__init_subclass__ = lambda x: TypeError()
    return cls

@final_class
class Unsubclassable():
    pass
```

Bonus 3:
Do it with metaclasses
The `bases != ()` doesn't work when you try to use the class decorator with it
```
class UnsubclassableType(type):
    def __new__(cls, name, bases, dctn, **kwargs):
        for base in bases:
            if isinstance(base, UnsubclassableType):
                raise TypeError("Trying to subclass Unsubclassable")
        return super().__new__(cls, name, bases, dctn)

class Unsubclassable(metaclass=UnsubclassableType):
    pass


def final_class(cls):
    return UnsubclassableType(cls.__name__, cls.__bases__, dict(cls.__dict__))
```


Given solution makes the `__init_subclass__` patched method a class method, which is something that I probably should've done
