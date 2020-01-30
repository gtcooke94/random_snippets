class Unpacker:

    """Class which attribute "unpacking"."""

    def __init__(self, mapping={}):
        self.__dict__ = dict(mapping)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return tuple(self.__dict__[k] for k in key)
        else:
            return self.__dict__[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            values = tuple(value)
            if len(key) != len(values):
                raise ValueError("Key/value length mismatch: {key} & {values}")
            self.__dict__.update(zip(key, values))
        else:
            self.__dict__[key] = value

    def __iter__(self):
        yield from self.__dict__.values()

    def __repr__(self):
        attrs = ", ".join(
            f"{key}={repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"Unpacker({attrs})"


'''
Using __getattr__ and __setattr__. Get around this by using the object's __dict__ with __getitem__ and __setitem__

class Unpacker:

    """Class which attribute "unpacking"."""

    def __init__(self, mapping={}):
        self.mapping = dict(mapping)

    def __getitem__(self, key):
        return self.mapping[key]

    def __setitem__(self, key, value):
        self.mapping[key] = value

    def __getattr__(self, item):
        return self.mapping[item]

    def __setattr__(self, attr, value):
        if attr == 'mapping':
            super().__setattr__(attr, value)
        else:
            self.mapping[attr] = value
'''
