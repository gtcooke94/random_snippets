# Base solution
def SliceView(sequence, start=None, stop=None, step=1):
    """A "view" into a sequence, like a "lazy slice"."""
    start, stop, step = slice(start, stop, step).indices(len(sequence))
    for i in range(start, stop, step):
        yield sequence[i]
