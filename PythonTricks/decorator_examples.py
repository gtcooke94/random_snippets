# A decorator is a callable that takes a callable as input and returns another
# callable.
def null_decorator(func):
    return func


# We don't have to do this because of the special python decorator syntax
def old_greet():
    return "Hello!"

old_greet = null_decorator(old_greet)
print(old_greet())


# With decorator syntax, this is the same as the above example where we create
# another function by calling the decorator function
# Decorates function at definition, difficult to access original function
@null_decorator
def greet():
    return "Hello!"

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet2():
    return "Hello!"

import time
def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print("Process took {} seconds".format(end_time - start_time))
        return result
    return wrapper


@timer
def greet3():
    return "Greet 3"


@timer
def greet4():
    time.sleep(2)
    return "Greet 4"

# Decorators with arguments
def trace(func):
    def wrapper(*args, **kwargs):
        print('TRACE: calling {}() '
              'with {}, {}'.format(func.__name__, args, kwargs))
        original_result = func(*args, **kwargs)
        print('TRACE: {}() '
              'returned {}'.format(func.__name__, original_result))
        return original_result
    return wrapper


@trace
def say(name, line):
    return "{}: {}".format(name, line)


# Using functools to keep information about the underlying function
# Applying to wrapper closure returned by decorator carriers over dicstring and
# other metadata of input function
import functools

def uppercase2(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase2
def say_hi():
    """Return a friendly greeting."""
    return "Hi!"

# The functools.wraps keeps this information as say_hi and the docstring rather
# than the information for the function "wrapper" in the decorator
print(say_hi.__name__)
print(say_hi.__doc__)
    
