#  class Repeater:
#      def __init__(self, value):
#          self.value = value
#
#      def __iter__(self):
#          return RepeaterIterator(self)
#
#  class RepeaterIterator:
#      def __init__(self, source):
#          self.source = source
#
#      def __next__(self):
#          return self.source.value
#
#  repeater = Repeater("Hello")
#  # This happens forever
#  #  for item in repeater:
#  #      print(item)
#
#  iterator = repeater.__iter__()
#  # Above for loop is equivalent to this
#  #  while True:
#  #      item = iterator.__next__()
#  #      print(item)
#
#  # Emulate behavior, replace __iter__ and __next__ with iter() and next()
#  it = iter(repeater)
#  next(it)
#  next(it)
#
#

# New, better repeater
class Repeater:
    def __init__(self, value):
        self.value = value

    # __iter__ must return any object with a __next__ method associated with it
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater("Hey", 5)
for item in repeater:
    print(item)

repeater = BoundedRepeater("No syntactic sugar", 3)
it = iter(repeater)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print(item)
