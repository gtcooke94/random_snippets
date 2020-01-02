from collections import UserString

class MutableString(UserString):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_slice(self, s):
        start, stop, step = s.start, s.stop, s.step

        if not start:
            start = 0
        if not stop:
            stop = len(self)
        if not step:
            step = 1

        return start, stop, step


    def __setitem__(self, s, val):
        strlist = list(self.data)
        if isinstance(s, int):
            strlist[s] = val
        elif isinstance(s, slice):
            strlist[s] = list(val)
        else:
            raise ValueError("Trying to slice with bad type")
        self.data = "".join(strlist)

    def __delitem__(self, s):
        self.__setitem__(s, "")

    def append(self, val):
        self.data = self.data + val

    def insert(self, loc, val):
        strlist = list(self.data)
        strlist.insert(loc, val)
        self.data = "".join(strlist)

    def pop(self, loc=-1):
        to_return = self[loc]
        del self[loc]
        return to_return
