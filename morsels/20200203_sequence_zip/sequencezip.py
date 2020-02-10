from collections.abc import Sequence


class SequenceZip(Sequence):
    def __init__(self, *seqs):
        self.lens = [len(seq) for seq in seqs]
        self.min_length = min(self.lens)
        self.seqs = seqs
        #  self.seqs = [seq[:self.min_length] for seq in seqs]

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.min_length + s
            return tuple(seq[s] for seq in self.seqs)
        else:
            start, stop, step = s.indices(self.min_length)
            if stop == -1:
                stop = None
            new_slice = slice(start, stop, step)
            return SequenceZip(*(seq[new_slice] for seq in self.seqs))

    def __len__(self):
        return self.min_length

    def __repr__(self):
        inside = ", ".join(repr(seq) for seq in self.seqs)
        return f"SequenceZip({inside})"

    def __eq__(self, o):
        if not isinstance(o, self.__class__):
            return False
        #  return all(a == b for a, b in zip(self, o))
        return all(
            seq1[: self.min_length] == seq2[: self.min_length]
            for seq1, seq2 in zip(self.seqs, o.seqs)
        )

    # Another option:
    #  def __eq__(self, other):
    #      if not isinstance(other, SequenceZip):
    #          return NotImplemented
    #      a = tuple(s[: len(self)] for s in self.sequences)
    #      b = tuple(s[: len(self)] for s in other.sequences)
    #      return a == b
