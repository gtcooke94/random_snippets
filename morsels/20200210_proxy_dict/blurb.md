For the base and bonus 1, the following worked wonderfully:
```
from collections import UserDict

class ProxyDict(UserDict):
    def __init__(self, d):
        self.data = d

    def __setitem__(self, key, value):
        raise TypeError("ProxyDict doesn't support item assignment")

    def pop(self):
        raise TypeError("ProxyDict doesn't support pop")
```

However, with bonus 2 needing to have multiple mappings, we needed something different. We couldn't just keep an updated single dict, because if something is deleted from the dict that ProxyDict is pointing to, it won't know, but needs to reflect the change. So, everything is based on building the `single_dict` when it is needed.
There may be a fancy way to implement this and still get the benefits of UserDict by making self.data be a property that returns `single_dict()`. But for now, I ripped out `UserDict` and had to implement all of the dict-like functions myself.


It was fairly trivial to do the above: Below first is the implementation using `self.data` as a property that builds the dictionary out of the collection. I think this is the better implemention. Second is the one that doesn't inherit from `UserDict` at all.
```

from collections import UserDict


class ProxyDict(UserDict):
    def __init__(self, *dicts):
        self.maps = list(dicts)

    @property
    def data(self):
        return {k: v for d in self.maps for k, v in d.items()}

    def __setitem__(self, key, value):
        raise TypeError("ProxyDict doesn't support item assignment")

    def pop(self):
        raise TypeError("ProxyDict doesn't support pop")

    def __repr__(self):
        inside = ", ".join(repr(d) for d in self.maps)
        return f"ProxyDict({inside})"
```


Worse implementation without inheriting from `UserDict`
```

class ProxyDict:
    def __init__(self, *dicts):
        self.maps = list(dicts)
        self.dicts = dicts[::-1]

    def __setitem__(self, key, value):
        raise TypeError("ProxyDict doesn't support item assignment")

    def pop(self):
        raise TypeError("ProxyDict doesn't support pop")

    def __getitem__(self, k):
        for d in self.dicts:
            try:
                return d[k]
            except KeyError:
                continue
        raise KeyError()

    def single_dict(self):
        return {k: v for d in self.dicts[::-1] for k, v in d.items()}

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.single_dict() == other.single_dict()
        else:
            return self.single_dict() == other

    def items(self):
        return self.single_dict().items()

    def values(self):
        return self.single_dict().values()

    def keys(self):
        return self.single_dict().keys()

    def __iter__(self):
        return iter(self.single_dict())

    def __len__(self):
        return len(self.single_dict())

    def get(self, k, default=None):
        try:
            return self.__getitem__(k)
        except KeyError:
            return default

    def __repr__(self):
        inside = ", ".join(repr(d) for d in self.maps)
        return f"ProxyDict({inside})"
```
