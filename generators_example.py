import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Process took {} seconds".format(end_time - start_time))
        return result
    return wrapper

@timeit
def with_generator(size):
    print("Generator:")
    generator_object = (i for i in range(size))
    for i in generator_object:
        i + 1

@timeit
def with_list(size):
    print("List:")
    list_object = [i for i in range(size)]
    for i in list_object:
        i + 1


if __name__ == "__main__":
    sizes = (int(s) for s in (1E8, 1E9, 1E10, 1E11))
    for size in sizes:
        print(size)
        with_generator(size)
        with_list(size)
    


    

