from collections import UserDict

class PermaDict(UserDict):
    def __init__(self, *args, silent=False, **kwargs):
        self.silent = silent
        super().__init__(*args, **kwargs)
    
    def __setitem__(self, k, v):
        if k in self:
            if self.silent:
                return
            raise KeyError(f"'{k}' already in dictionary.")
        super().__setitem__(k, v)

    def force_set(self, key, val):
        super().__setitem__(key, val)

    def update(self, *args, force=False, **kwargs):
        if force:
            self.data.update(*args, **kwargs)
        else:
            super().update(*args, **kwargs)

    #  def update(self, *args, force=False, **kwargs):
    #      if force:
    #          self.__setitem__ = super().__setitem__
    #      super().update(*args, **kwargs)
    #      self.__setitem__ = self.perma_set_item
    #
    #  __setitem__ = perma_set_item


#  if __name__ == "__main__":
#      d1 = PermaDict({2:3})
#      d1[3] = 4
#      try:
#          d1[2] = 1000
#      except KeyError:
#          pass
#      print(d1)
#
