from suppress import suppress

with suppress(KeyError, TypeError):
    a = 5
