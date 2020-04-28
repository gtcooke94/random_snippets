class UnsubclassableType(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        for base in bases:
            if isinstance(base, UnsubclassableType):
                raise TypeError(
                    "type '{base.__name__}' is not an acceptable base type"
                )
        self = super().__new__(cls, name, bases, namespace)
        return self


def final_class(cls):
    @classmethod
    def no_subclass(subclass):
        class_name = cls.__name__
        subclass_name = subclass.__name__
        raise TypeError(f"Class {subclass_name} cannot subclass {class_name}")
    cls.__init_subclass__ = no_subclass
    return cls


@final_class
class Unsubclassable:
    pass
