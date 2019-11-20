def interleave(*lists):
    num_iterables = len(lists)
    current_iterable = 0
    
    iterables = [iter(l) for l in lists]
    pass_counter = 0

    while True:
        if pass_counter == num_iterables:
            break
        try:
            yield next(iterables[current_iterable])
            pass_counter = 0
        except:
            pass_counter += 1
            pass
        current_iterable = (current_iterable + 1) % num_iterables
