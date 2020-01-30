# My rewrite attempt at a better solution
class Unpacker:
    def __init__(self, data={}):
        # Make sure to copy the mutable default:
        self.__dict__ = dict(data)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return tuple(self.__getitem__(k) for k in key)
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            keys = key
            values = tuple(value)
            if len(values) != len(keys):
                raise ValueError()
            for k, v in zip(keys, values):
                self.__setitem__(k, v)
            # Could do self.__dict__.update(zip(keys, values)) instead of the loop
        else:
            self.__dict__[key] = value

    def __iter__(self):
        return iter(self.__dict__.values())
        # Or
        #  yield from self.__dict__.values()

    def __repr__(self):
        inside = ", ".join(
            f"{key}={repr(value)}" for key, value in self.__dict__.items()
        )
        return f"Unpacker({inside})"


# Original working solution
#  from collections import UserDict
#
#  MISSING_VALUE = object()
#
#  class Unpacker(UserDict):
#      def __init__(self, data=None):
#          self.data = data
#          if data:
#              super().__init__(data)
#          else:
#              super().__init__()
#          for k, v in self.data.items():
#              setattr(self, k, v)
#
#      def __getitem__(self, k):
#          """ if dict is updated, attribute is updated. If attribute is updated, dict is NOT updated.
#          Make sure the dict and attribute are equal. If not, attribute is the ground truth"""
#          if isinstance(k, tuple):
#              return tuple(self.get_single_item(key) for key in k)
#          else:
#              return self.get_single_item(k)
#
#      def get_single_item(self, k):
#          if not getattr(self, k) == self.data.get(k, MISSING_VALUE):
#              self.data[k] = getattr(self, k)
#          return super().__getitem__(k)
#
#      def __setitem__(self, k, v):
#          if isinstance(k, tuple):
#              k = list(k)
#              v = list(v)
#              if len(k) != len(v):
#                  raise ValueError()
#              for key, value in zip(k, v):
#                  self.set_single_item(key, value)
#          else:
#              self.set_single_item(k, v)
#
#      def set_single_item(self, k, v):
#          super().__setitem__(k, v)
#          setattr(self, k, v)
#
#      def __iter__(self):
#          yield from self.data.values()
#
#      def __repr__(self):
#          inside = ", ".join(f"{k}={repr(v)}" for k, v in self.data.items())
#          return f"Unpacker({inside})"


#  class Unpacker(UserDict):
#      def __init__(self, data=None):
#          self.data = data
#          if data:
#              super().__init__(data)
#          else:
#              super().__init__()
#          # Instead of keeping two dicts that are the same and having to update both, just make self.data and self.__dict__ point at the same dict! HORRIBLE!!!! We have a recursive definition :(
#          # It seems we will also want to keep things in our "data" separate from __dict__
#
#          self.__dict__.update(**self.data)
#          self.data = self.__dict__
