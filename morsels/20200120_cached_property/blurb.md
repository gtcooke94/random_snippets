Try 1.
Generally works, but breaks if the value is actually supposed to be None, and if there are multiple of the same class (this creates a cache for the whole class)

```
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = None

    def __get__(self, obj, objtype):
        if self.cache is not None:
            return self.cache
        self.cache = obj.__dict__[self.fn.__name__] = self.fn(obj)
        return self.cache
```

Try 2.
Add a sentinel value. This still fails the test for multiple instances of the class

```
NO_VALUE = object()
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = NO_VALUE

    def __get__(self, obj, objtype):
        if self.cache is not NO_VALUE:
            return self.cache
        self.cache = obj.__dict__[self.fn.__name__] = self.fn(obj)
        return self.cache
```

Try 3.
```
This solves the multiple instance issue - have the cache be a dict of instance to value! What a great idea. Unforunately, it causes a memory leak, so it's bad as well. The dict stores a pointer to obj, so when object gets deleted by python, there is still a reference to it in this dictionary.
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        #  self.cache = NO_VALUE
        self.cache = {}

    # MEMORY LEAK!!!!
    def __get__(self, obj, objtype):
        if obj in self.cache:
            return self.cache[obj]
        self.cache[obj] = self.fn(obj)
        return self.cache[obj]
```

No-Bonus Solution:
Use the id of the object instead of the object itself. This should be unique for the life of the object. One thing that perhaps needs to be dealt with is making sure that if the object dies and another gets the same id that we don't have cache overlap. I'm not exactly sure how to test this though.
```
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __get__(self, obj, objtype):
        obj_id = id(obj)
        if obj_id in self.cache:
            return self.cache[obj_id]
        self.cache[obj_id] = self.fn(obj)
        return self.cache[obj_id]
```

Bonus 1 Solution:
    We need to add a __delete__ method for this bonus. A non-data descriptor only defines the __get__ method. A data descriptor defines __get__, __set__, and __delete__. So, if we want a __delete__ method, we have to have a __set__ method.
    

```
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __get__(self, obj, objtype):
        obj_id = id(obj)
        if obj_id in self.cache:
            return self.cache[obj_id]
        self.cache[obj_id] = obj.__dict__[self.fn.__name__] = self.fn(obj)
        return self.cache[obj_id]

    def __delete__(self, obj):
        del self.cache[id(obj)]

    def __set__(self, obj, val):
        self.cache[id(obj)] = val
```

Bonus 2 Solution:
    Now we need to be able to access this from the class. From tracing through with pdb, the __get__ is called with obj=None, klass = <calling class> when we do Thing.x (where thing is a class and x is the decorated cached property). So, if obj=None, we just return cached_property. Then we can call cached_propertys __get__ later

```
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __get__(self, obj, klass=None):
        if obj is None:
            return self
        obj_id = id(obj)
        if obj_id in self.cache:
            return self.cache[obj_id]
        self.cache[obj_id] = obj.__dict__[self.fn.__name__] = self.fn(obj)
        return self.cache[obj_id]

    def __delete__(self, obj):
        del self.cache[id(obj)]

    def __set__(self, obj, val):
        self.cache[id(obj)] = val
```

Bonus 3 Solution:
    Need to understand why this worked for setter and deleter. Through testing, I found that they needed return values. The deleter also needed to continue to update the cache and call the given function.


```
class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}
        self.fdel = None

    def __get__(self, obj, klass=None):
        if obj is None:
            return self
        obj_id = id(obj)
        if obj_id in self.cache:
            return self.cache[obj_id]
        self.cache[obj_id] = obj.__dict__[self.fn.__name__] = self.fn(obj)
        return self.cache[obj_id]

    def __delete__(self, obj):
        if self.fdel:
            self.fdel(obj)
        del self.cache[id(obj)]

    def __set__(self, obj, val):
        self.cache[id(obj)] = val

    def setter(self, fn):
        self.__set__ = fn
        return self

    def deleter(self, fn):
        self.fdel = fn
        return self
```

The final solutions that are provided are saved in `solutions.py`. The main difference between my solution and there's is that, rather than store the cache values in a dictionary keyed by the object id, the value is stored on the object itself. This gets around an issue I thought about above with potentially overlapping object ids.



