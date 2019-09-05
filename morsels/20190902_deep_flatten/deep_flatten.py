def deep_flatten(iterables):
    """Accept a list of lists (or list of tuples and lists) and return a flattened version"""
    for item in iterables:
        if is_iterable(item):
            yield from deep_flatten(item)
        else:
            yield item

def is_iterable(item):
    if isinstance(item, str):
        return False
    try:
        _ = iter(item)
        return True
    except TypeError:
        return False
