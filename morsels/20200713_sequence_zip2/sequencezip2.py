from collections.abc import Sequence

class SequenceZip(Sequence):
    def __init__(self, *seqs):
        self.seqs = seqs
        self._length = min(len(seq) for seq in self.seqs)

    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(len(self))
            if stop == -1:
                stop = None
            return SequenceZip(*(seq[start:stop:step] for seq in self.seqs))
        if isinstance(i, int) and i < 0:
            i = len(self) + i
        return tuple(seq[i] for seq in self.seqs)

    def __len__(self):
        return self._length

    def __eq__(self, other):
        return list(self) == list(other)
