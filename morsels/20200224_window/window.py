def window(iterable, window_size, *, fillvalue=None):
    if window_size == 0:
        return []
    it = iter(iterable)
    cur = []
    for _ in range(window_size):
        try:
            cur.append(next(it))
        except StopIteration:
            cur.extend([fillvalue] * (window_size - len(cur)))
            yield tuple(cur)
            return

    yield tuple(cur)

    while True:
        try:
            cur = cur[1:]
            cur.append(next(it))
            yield tuple(cur)
        except StopIteration:
            return
