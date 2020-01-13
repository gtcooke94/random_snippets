from itertools import cycle
from collections import UserList


class CyclicList(UserList):
    def __setitem__(self, s, val):
        length = len(self.data)
        if isinstance(s, int):
            self.data[s % length] = val

    def __getitem__(self, s):
        length = len(self.data)
        if isinstance(s, int):
            return self.data[s % length]
        if not s.start and not s.stop:
            return self.data
        if not s.start:
            start = 0
            real_start = 0
        else:
            real_start = s.start % length
            start = s.start
        if not s.stop:
            stop = 0
        else:
            stop = s.stop
        total = stop - start
        counter = 0
        j = real_start
        to_return = []
        while counter < total:
            to_return.append(self.data[j])
            j = (j + 1) % length
            counter += 1
        return to_return

    # Don't need __iter__ if you have UserList and __getitem__    
    #  def __iter__(self):
    #      return cycle(self.data)


################################################################################
# His solution
#  class CyclicList(UserList):
#      def _slice_indices(self, obj):
#          start, stop = obj.start, obj.stop
#          if obj.step is not None:
#              raise ValueError("Step not supported")
#          if start is None:
#              start = 0
#          if stop is None:
#              stop = len(self) if start >= 0 else 0
#          return start, stop, 1
#
#      def __getitem__(self, index):
#          if isinstance(index, slice):
#              return [
#                  self[i]
#                  for i in range(*self._slice_indices(index))
#              ]
#          return self.data[index % len(self)]
#
#      def __setitem__(self, index, value):
#          self.data[index % len(self)] = value
