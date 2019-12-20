def strict_zip(*args):
    if not args:
        return
    iters = [iter(a) for a in args]
    while True:
        items = []
        all_excepted = [False] * len(args)
        for i in range(len(args)):
            try:
                items.append(next(iters[i]))
            except StopIteration:
                all_excepted[i] = True
                continue
        if all(all_excepted):
            return
        if any(all_excepted):
            raise ValueError("value out of range")
        yield tuple(items)
