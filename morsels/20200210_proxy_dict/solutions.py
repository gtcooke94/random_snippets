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
