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

    def __repr__(self):
        return f"ChainSequence({', '.join(repr(s) for s in self.sequences)})"

    def __add__(self, other):
        return ChainSequence(*self.sequences, other)

    def __iadd__(self, other):
        self.sequences.append(other)
        return self



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
