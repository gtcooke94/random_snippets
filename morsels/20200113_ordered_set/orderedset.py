from collections import UserList

class OrderedSet(UserList):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.set = set()
        i = 0
        while i < len(self.data):
            val = self.data[i]
            if val in self.set:
                del self.data[i]
            else:
                self.set.add(val)
                i += 1

    def __contains__(self, val):
        return val in self.set

    def add(self, val):
        if val not in self.set:
            self.set.add(val)
            self.data.append(val)

    def discard(self, val):
        if val in self.set:
            self.set.discard(val)
            del self.data[self.data.index(val)]

    def __eq__(self, other):
        if isinstance(other, set):
            return self.set == other
        elif isinstance(other, self.__class__):
            return self.data == other.data
        else:
            return False

# PythonMorsels Solution
# It's better
#  from collections.abc import MutableSet, Sequence
#
#  class OrderedSet(Sequence, MutableSet):
#      def __init__(self, iterable):
#          self.items = set()
#          self.order = []
#          self |= iterable
#
#      def __contains__(self, item):
#          return item in self.items
#
#      def __len__(self):
#          return len(self.items)
#
#      def __getitem__(self, index):
#          return self.order[index]
#
#      def add(self, item):
#          if item not in self.items:
#              self.order.append(item)
#              self.items.add(item)
#      def discard(self, item):
#          if item in self.items:
#              self.order.remove(item)
#              self.items.remove(item)
#
#      def __eq__(self, other):
#          if isinstance(other, type(self)):
#              return (
#                  len(self) == len(other) and
#                  all(x == y for x, y in zip(self, other))
#              )
#          return super().__eq__(other)
