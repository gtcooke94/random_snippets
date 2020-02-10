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


#  # Full Solution
#  class ProxyDict:
#      def __init__(self, *dicts):
#          self.maps = list(dicts)
#          self.dicts = dicts[::-1]
#
#      def __setitem__(self, key, value):
#          raise TypeError("ProxyDict doesn't support item assignment")
#
#      def pop(self):
#          raise TypeError("ProxyDict doesn't support pop")
#
#      def __getitem__(self, k):
#          for d in self.dicts:
#              try:
#                  return d[k]
#              except KeyError:
#                  continue
#          raise KeyError()
#
#      def single_dict(self):
#          return {k: v for d in self.dicts[::-1] for k, v in d.items()}
#
#      def __eq__(self, other):
#          if isinstance(other, type(self)):
#              return self.single_dict() == other.single_dict()
#          else:
#              return self.single_dict() == other
#
#      def items(self):
#          return self.single_dict().items()
#
#      def values(self):
#          return self.single_dict().values()
#
#      def keys(self):
#          return self.single_dict().keys()
#
#      def __iter__(self):
#          return iter(self.single_dict())
#
#      def __len__(self):
#          return len(self.single_dict())
#
#      def get(self, k, default=None):
#          try:
#              return self.__getitem__(k)
#          except KeyError:
#              return default
#
#      def __repr__(self):
#          inside = ", ".join(repr(d) for d in self.maps)
#          return f"ProxyDict({inside})"


# Base and Bonus 1 Solution
#  from collections import UserDict
#
#  class ProxyDict(UserDict):
#      def __init__(self, d):
#          self.data = d
#
#      def __setitem__(self, key, value):
#          raise TypeError("ProxyDict doesn't support item assignment")
#
#      def pop(self):
#          raise TypeError("ProxyDict doesn't support pop")
