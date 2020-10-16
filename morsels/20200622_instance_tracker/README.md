### Base Solution

Need to construct a new instance_tracker everytime. Because it gets called as
`class Account(instance_tracker())`, we correctly want a different one for each class it gets put it.

The `super().__init__(...)` has to happen because of multiple inheritance/inheritance chains.

```
def instance_tracker():
    class InstanceTracker:
        instances = []
        def __init__(self, *args, **kwargs):
            self.instances.append(self)
            super().__init__(*args, **kwargs)
    return InstanceTracker
```


### Bonus 1:

Tried to do some stuff with `__new__` and `__init__`, but kept running into snags
Essentially was trying to do `setattr(type(self))` and `getattr(type(self))`, but that didn't work how I wanted it to. In the end just needed to add the line right before the return.

Can definitely do this in a metaclass way, but I don't want to have to reach to that yet.

```
def instance_tracker(tracker_list_name="instances"):
    class InstanceTracker:
        instances = []
        def __init__(self, *args, **kwargs):
            if not hasattr(self, tracker_list_name):
                setattr(self.__class__, tracker_list_name, [])
            getattr(self, tracker_list_name).append(self)
            super().__init__(*args, **kwargs)

    setattr(InstanceTracker, tracker_list_name, InstanceTracker.instances)
    return InstanceTracker
```

### Bonus 2:
This bonus is to make sure it works if we don't ensure subclasses call `__init__`... so the above doesn't work at all, the code can't be in the `__init__`, because there's no guarantee it's going to get called.

BUT! `__new__` will get called (right?). Need to do some more reading on this.
This works though. Essentially, when _contructing_ a new instance, make sure it has the `tracker_list_name` list in the class, construct the instance, 

This looks a little funky because it looks like we append instances to `tracker_list_name`, then replace `tracker_list_name` when the empty list `instances`. BUT, that `setattr` happens before anything in `__new__` every runs, so the two lists are linked to the same list in memory before either every has any contents :)

It makes a little more sense if you replace `setattr(cls, tracker_list_name, [])` with `setattr(cls, tracker_list_name, cls.instances)`

```
def instance_tracker(tracker_list_name="instances"):
    class InstanceTracker:
        instances = []
        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, tracker_list_name):
                setattr(cls, tracker_list_name, [])
            instance = super().__new__(cls)
            getattr(instance, tracker_list_name).append(instance)
            return instance

    setattr(InstanceTracker, tracker_list_name, InstanceTracker.instances)
    return InstanceTracker
```


### Bonus 3:
Having weak references  is made easier with the `weakref` module
I tried to have a list of `weakref.ref`s first, but that didn't work. So instead I think a `WeakSet` is the right answer.

```
import weakref


def instance_tracker(tracker_list_name="instances"):
    class InstanceTracker:
        instances = weakref.WeakSet()

        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, tracker_list_name):
                setattr(cls, tracker_list_name, cls.instances)
            instance = super().__new__(cls)
            getattr(instance, tracker_list_name).add(instance)
            return instance

    setattr(InstanceTracker, tracker_list_name, InstanceTracker.instances)
    return InstanceTracker
```



After looking at the solutions, we can make this even cleaner
```
import weakref


def instance_tracker(tracker_list_name="instances"):
    class InstanceTracker:
        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            getattr(cls, tracker_list_name).add(instance)
            return instance

    setattr(InstanceTracker, tracker_list_name, weakref.WeakSet())
    return InstanceTracker
```
