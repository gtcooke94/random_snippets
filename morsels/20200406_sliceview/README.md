I incorrectly made the assumption that I had to handle iterators in mine as well, but it seems we were okay to handle sequences (which should've been clear to me, because I had to use the length function anyways).
My solution is very overcomplicated because I didn't assume I could index into the sequence, but rather had to iterate through it.

The base solution, for example, is far far simpler than mine
```
# Base solution
def SliceView(sequence, start=None, stop=None, step=1):
    """A "view" into a sequence, like a "lazy slice"."""
    start, stop, step = slice(start, stop, step).indices(len(sequence))
    for i in range(start, stop, step):
        yield sequence[i]

```

Need to spend more time with Bonus 1, making it a reusable iterator. Goes down to making `__iter__` a generator function rather than `return self` and make a `__next__` method.


Full answer doesn't even need `__iter__` at all - if you have `__getitem__` and `__len__`, you are iterable!
```
from collections.abc import Sequence


class SliceView(Sequence):
    """A "view" into a sequence, like a "lazy slice"."""
    def __init__(self, sequence, start=None, stop=None, step=None):
        start, stop, step = slice(start, stop, step).indices(len(sequence))
        self.range = range(start, stop, step)
        self.sequence = sequence
    def __len__(self):
        return len(self.range)
    def __getitem__(self, index):
        if not isinstance(index, slice):
            return self.sequence[self.range[index]]
        else:
            return SliceView(self, index.start, index.stop, index.step)
```
