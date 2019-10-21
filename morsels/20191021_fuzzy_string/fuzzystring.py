import unicodedata


class FuzzyString:
    def __init__(self, string):
        self.string = string

    def _normalize_string(self, o):
        return unicodedata.normalize("NFD", o.upper().lower())

    def __eq__(self, o):
        if isinstance(o, str):
            return self._normalize_string(self.string) == self._normalize_string(o)

    def __gt__(self, o):
        return self._normalize_string(self.string) > self._normalize_string(o)

    def __lt__(self, o):
        return self._normalize_string(self.string) < self._normalize_string(o)

    def __le__(self, o):
        return self._normalize_string(self.string) <= self._normalize_string(o)

    def __ge__(self, o):
        return self._normalize_string(self.string) >= self._normalize_string(o)

    def __ne__(self, o):
        return not self == o

    def __str__(self):
        return self.string

    def __repr__(self):
        return repr(self.string)

    def __contains__(self, item):
        return item.lower() in self._normalize_string(self.string)

    def __add__(self, o):
        return FuzzyString(self.string + o)
