## Base Problem
Using `Sequence` makes everything a little bit easier, and you just have to implement `__getitem__` and `__len__`
```
from collections.abc import Sequence

class SequenceZip(Sequence):
    def __init__(self, *seqs):
        self.seqs = seqs
        self._length = min(len(seq) for seq in self.seqs)

    def __getitem__(self, i):
        if i < 0:
            i = len(self) + i
        return tuple(seq[i] for seq in self.seqs)

    def __len__(self):
        return self._length

    def __eq__(self, other):
        return list(self) == list(other)
```

## Adding slicing with this kind of thing is always a little bit tricky
I don't fully understand why this line works, I always have trouble converting between slicing and raw indices
`stop = -(len(self) + 1 - stop)`

```
from collections.abc import Sequence

class SequenceZip(Sequence):
    def __init__(self, *seqs):
        self.seqs = seqs
        self._length = min(len(seq) for seq in self.seqs)

    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(len(self))
            if step < 0:
                # TODO, understand exactly why this works
                stop = stop = -(len(self) + 1 - stop)
            return SequenceZip(*(seq[start:stop:step] for seq in self.seqs))
        if isinstance(i, int) and i < 0:
            i = len(self) + i
        return tuple(seq[i] for seq in self.seqs)

    def __len__(self):
        return self._length

    def __eq__(self, other):
        return list(self) == list(other)
```

See below exploration:
```
In [38]: test
Out[38]: [1, 2, 3, 4]

In [39]: slice(2, None, -1).indices(4)
Out[39]: (2, -1, -1)

In [40]: test[3:-6:-1]
Out[40]: [4, 3, 2, 1]

In [41]: test
Out[41]: [1, 2, 3, 4]

In [42]: test[3:-10:-1]
Out[42]: [4, 3, 2, 1]

In [43]: test = [1, 2, 3, 4]

In [44]: test[::-1]
Out[44]: [4, 3, 2, 1]

In [45]: s = slice(None, None, -1)

In [46]: start, stop, step = s.indices(len(test))

In [47]: print(start, stop, step)
3 -1 -1

In [48]: stop = -(len(test) + 1 - stop)

In [49]: print(start, stop, step)
3 -6 -1

In [50]: test[3:-6:-1]
Out[50]: [4, 3, 2, 1]
```


On further exploration, I'm not convinced this works completely
For example, I added this test and it fails
```
seq = SequenceZip(range(6), [1, 2, 3, 4], 'hiya!!', range(1000))
self.assertEqual(list(seq[:2:-1]), [
    (3, 4, "a", 3)
])
```


I believe this implementation of handling the slicing is correct
The issue comes from `slice.indices` not following the expected rules of negatives. Rather, a `-1` returned from `indices` actually means to include 0 when going in reverse, because it represent the non-inclusive stop index. However, using that in a `slice` object returns to it's meaning as "one from the back", whereas `None` represents including the very first element.
```
def __getitem__(self, i):
    if isinstance(i, slice):
        start, stop, step = i.indices(len(self))
        if stop == -1:
            stop = None
        return SequenceZip(*(seq[start:stop:step] for seq in self.seqs))
    if isinstance(i, int) and i < 0:
        i = len(self) + i
    return tuple(seq[i] for seq in self.seqs)
```
