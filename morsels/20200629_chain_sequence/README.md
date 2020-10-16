### Base problem

I was trying to get fancy with `chain`, but just decided to do it the simple way.
Mathematically calculate which sequence an index corresponds to, then get that index

```
from collections.abc import Sequence


class ChainSequence(Sequence):
    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __getitem__(self, i):
        subsequence, ind_in_subsequence = self.determine_subsequence(i)
        return subsequence[ind_in_subsequence]

    def determine_subsequence(self, i):
        total_length = 0
        if i < 0:
            i = len(self) + i
        if i >= len(self):
            raise IndexError
        for subsequence_num, subsequence_len in enumerate(
            len(s) for s in self.sequences
        ):
            total_length += subsequence_len
            if total_length > i:
                break

        return self.sequences[subsequence_num], i - (total_length - subsequence_len)

    def __len__(self):
        return sum(len(s) for s in self.sequences)
```

### Bonus 1
Looked at solution for inspiration, glad I did. It's very clean!
`SliceView` smartly uses the implemented `__getitem__`, so there's really nothing extra to implement!
```
from collections.abc import Sequence


class ChainSequence(Sequence):
    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __getitem__(self, i):
        if  isinstance(i, slice):
            return SliceView(self, start=i.start, stop=i.stop, step=i.step)
        if i < 0:
            i = len(self) + i
        if i >= len(self):
            raise IndexError

        for sequence in self.sequences:
            if i < len(sequence):
                return sequence[i]
            i -= len(sequence)

    def __len__(self):
        return sum(len(s) for s in self.sequences)



# Provided SliceView
class SliceView(Sequence):
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

### Bonus 2
Just a nice repr. Gotta make it strings joined together, originally tried to just do `{repr(s) for s in self.sequences}`, but that made the repr just print a list/generator thing
```
    def __repr__(self):
        return f"ChainSequence({', '.join(repr(s) for s in self.sequences)})"
```
### Bonus 3
Adding lists to chain sequences is easy:
```
    def __add__(self, other):
        return ChainSequence(*self.sequences, other)

    def __iadd__(self, other):
        self.sequences.append(other)
        return self
```
