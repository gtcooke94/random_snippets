from math import ceil

class SliceView:
    def __init__(self, seq, start=None, stop=None, step=1):
        self.seq_length = len(seq)
        self.seq = seq
        s = slice(start, stop, step)
        self.start = s.indices(self.seq_length)[0]
        self.stop = s.indices(self.seq_length)[1]
        if step is None:
            step = 1
        self.base_step = step
        self.step = step
        self.handle_negative_step()

    def handle_negative_step(self):
        if self.step < 0:
            self.step = -self.step
            self.start = self.seq_length - self.start - 1
            self.stop = self.seq_length - self.stop - 1

    def initialize_iteration(self):
        if self.base_step < 0:
            self.it = iter(reversed(self.seq))
        else:
            self.it = iter(self.seq)

        self.counter = self.start
        for i in range(self.start):
            temp = next(self.it)
            print(f"Tossing index {i}, value {temp}")

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = len(self) + s
            self.initialize_iteration()
            for i in range(s):
                next(self.it)
            return next(self.it)
        return SliceView(self, start=s.start, stop=s.stop, step=s.step)

    def __iter__(self):
        self.initialize_iteration()
        return self

    def __next__(self):
        if self.counter >= self.stop:
            raise StopIteration()
        self.counter += self.step
        temp = next(self.it)
        print(f"Iterating, returning {temp}")
        for _ in range(self.step - 1):
            next(self.it)
        return temp

    def __len__(self):
        return ceil((self.stop - self.start) / self.step)

