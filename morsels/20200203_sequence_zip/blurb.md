At first, I tried to deal with wrong-length sequences by doing `self.seqs = [seq[:self.min_length] for seq in seqs]`. However, this generates copies of the sequences which is not desirable behavior. Instead, I deal with longer sequences in the `__getitem__` method by doing.
```
    def __getitem__(self, s):
        if s < 0:
            s = self.min_length + s
        return tuple(seq[s] for seq in self.seqs)
```
Non-negative indices are fine, and by using the `Sequence` ABC, we get iteration by implementing `__getitem__` and `__len__`. My guess is under the hood, the iteration that `Sequence` does is something like the following:
```
for i in range(len(self)):
    yield self.__getitem__(i)
```
My sequence correctly iterates to the length defined by `__len__` and doesn't go beyond, so it doesn't matter that I keep the sequences of longer length, therefore I don't have to worry about slicing (and therefore, copying) them.

For bonus 1, we need the `isinstance` check so it will fails against non-SequenceZips (desired behavior). In addition, we want to do sequence to sequence comparison rather than element to element comparison.
So, while `all(a == b for a, b in zip(self, o))` works, it doesn't compare the underlying `self.seqs`. However, we hit a slight snag since we don't cut the sequences beforehand, so to compare those we do have to do a slice:

`return all(seq1[:self.min_length] == seq2[:self.min_length] for seq1, seq2 in zip(self.seqs, o.seqs))`


Bonus 3 was some slicing stuff, and using `slice.indices()` was very useful. It didn't behave quite like I thought it would with `::-x` arguments. For example:
```
a = list(range(10))
s = slice(None, None, -1)
start, stop, step = s.indices(len(a)) # Gets 9, -1, -1
a[slice(start, stop, step)] # Gets []
a[s] # Gets [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

I actually went through the Python-ideas list and found where Guido wasn't very happy with this `-1`. The issue is that generally, in Python `thing[-x]` means "thing[len(thing) - x]". However, in this specific return, `-1` means ""1 left of 0", because we want to get thing things at index 9 to 0 INCLUSIVE, so `-1` is the exclusive range when going backwards.
