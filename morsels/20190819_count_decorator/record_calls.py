from functools import wraps


NO_RETURN = object()


class CallInfo:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.return_value = NO_RETURN
        self.exception = None


def record_calls(func):
    # The wraps decorator keeps docstrings and such nicely
    @wraps(func)
    def counted(*args, **kwargs):
        # We can reference the function itself :)
        counted.calls.append(CallInfo(*args, **kwargs))
        # Must do this or get reference error for result later
        result = NO_RETURN
        try:
            # Record arguments and results
            result = func(*args, **kwargs)
            counted.calls[counted.call_count].return_value = result
        except Exception as e:
            counted.calls[counted.call_count].exception = e
            raise e
        counted.call_count += 1
        return result

    # Remember, this stuff only happens when we originally decorate the function - after that, counted will get called
    counted.call_count = 0
    counted.calls = []
    return counted
