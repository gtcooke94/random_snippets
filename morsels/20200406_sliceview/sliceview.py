class SliceView:
    def __init__(self, seq, start=None, stop=None, step=1):
        self.seq_length = len(seq)
        self.seq = seq
        s = slice(start, stop, step)
        self.start = s.indices(self.seq_length)[0]
        self.stop = s.indices(self.seq_length)[1]
        self.base_step = step
        self.step = step
        #  self.initialize_iteration()

    def initialize_iteration(self):
        if self.base_step < 0:
            self.it = iter(reversed(self.seq))
            self.step = -self.base_step
            self.start = self.seq_length - self.start - 1
            self.stop = self.seq_length - self.stop - 1
        else:
            self.it = iter(self.seq)

        self.counter = self.start
        for i in range(self.start):
            temp = next(self.it)
            print(f"Tossing index {i}, value {temp}")

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

    #  def __len__(self):
    #      return (self.stop - self.start) // self.step

