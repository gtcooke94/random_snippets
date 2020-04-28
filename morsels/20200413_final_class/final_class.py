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

