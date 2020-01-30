# Base problem
I am making a dictionary-like object, so I want to inherit from UserDict

Linking __dict__ to self.data works, but is recursive. This didn't break my tests, but I think it should've. There's probably also a better way to do this (not subclassing dict and writing all of the dict methods I guess would've worked)

Base problem just had to deal with keeping `self.data` and `self.__dict__` up to date. `self.data` was accessed when doing indexing, and `self.__data__` was access when doing `object.attribute` notation.

Came upon the problem that doing `object.attribute = value` updates `__dict__`, but doesn't update `self.data`. So, when that value is gotten, we just check to make sure `__dict__` and `self.data` match, and if they don't the `__dict__` is the ground truth, because it is definitely updated when `self.data` is updated (in our implementation).

Bonus 1 was easy, assuming our dictionary is ordered (Python 3.?+), as we just iterate through the keys

Bonus 2 was a slight pain to get the quotes matching for string repr, but some fiddling got it working

Bonus 3 required changes to __getitem__ and __setitem__. Good thing to know - if you attempt to do "multi-dimensional indexing" like `object["a, "b"]`, it still calls the same methods (`__getitem__`, `__setitem__`), and passes in all indices as a single argument that is a tuple. So I just renamed my previous functions that did single item get/set, then called those from `__getitem__` and `__setitem__` for each individual item passed through.


The solution given is defintely better than my approach. I thought of linking `__dict__` to the `self.data` of `UserDict`, but the better solution was to just not use `UserDict` at all. This is an example of where I made a bad design choice early and could've done much better abadoning it.





