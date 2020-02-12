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



I've included solutions of note below. `MappingProxyType` is exactly what we want without the multiple dict bonus. `ChainMap` allows us to easily solve the multiple dict bonus. The `ChainMap` and `MappingProxyType` solution is a little too clever and hard to grok I think. Last below would be if we didn't want to use `ChainMap`. I think overall I like it more than mine - I inherited from `UserDict`, but then had to take features _out_. That's worse design than inheriting from `Mapping` and _adding_ features, and I'm sure it would be easy for somebody to have bugs with my `UserDict` solution.

```
from collections import ChainMap
from collections.abc import Mapping


class ProxyDict(Mapping):
    def __init__(self, *mappings):
        self.mappings = ChainMap(*reversed(mappings))

    def __getitem__(self, key):
        return self.mappings[key]

    def __iter__(self):
        return iter(self.mappings)

    def __len__(self):
        return len(self.mappings)

    def __repr__(self):
        class_name = type(self).__name__
        map_reprs = ', '.join(repr(m) for m in self.maps)
        return f"{class_name}({map_reprs})"

    @property
    def maps(self):
        return self.mappings.maps[::-1]

#  ================================================================================
from collections import ChainMap, UserDict
from types import MappingProxyType


class ProxyDict(UserDict):
    def __init__(self, *maps):
        self.chained = ChainMap(*reversed(maps))
        self.data = MappingProxyType(self.chained)
    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(m) for m in self.maps)})"
    @property
    def maps(self):
        return self.chained.maps[::-1]
#  ================================================================================
from collections.abc import Mapping


class ProxyDict(Mapping):

    """Immutable dictionary-wrapper class."""

    def __init__(self, *mappings):
        self.maps = list(mappings)

    def __repr__(self):
        class_name = type(self).__name__
        map_reprs = ', '.join(repr(m) for m in self.maps)
        return f"{class_name}({map_reprs})"

    def __getitem__(self, key):
        for mapping in reversed(self.maps):
            if key in mapping:
                return mapping[key]
        raise KeyError(key)

    def __len__(self):
        return len(self.keys())

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return {
            key
            for mapping in self.maps
            for key in mapping
        }
```
