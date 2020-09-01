## First attempt
First attempt, major bug

If there's multiple instances of the same class, this doesn't work at all.
Descriptors are instantiated on the CLASS DEFINITION, not per instance
```
# Major bug, this doesn't handle multiple instances of the same class
UNSET = object()

class computed_property:
    def __init__(self, attr):
        print(attr)
        self.linked_attr = attr
        self.linked_attr_value = UNSET
        self.computed_value = UNSET

    def __get__(self, obj, typ):
        # If nothing has been setup, set it up
        if obj is None:
            return self
        #  if getattr(obj, self.linked_attr, UNSET) is UNSET:
        #      return self
        if self.linked_attr_value is UNSET:
            self.computed_value = self.func(obj)
            self.linked_attr_value = getattr(obj, self.linked_attr)
        elif self.linked_attr_value != getattr(obj, self.linked_attr):
            self.computed_value = self.func(obj)
            self.linked_attr_value = getattr(obj, self.linked_attr)
        return self.computed_value

    def __set__(self, obj, value):
        raise AttributeError(f"Can't set {self.name}")

    def __call__(self, func, *args, **kwargs):
        self.func = func
        return self

    def __set_name__(self, obj, name):
        self.cached_attr = name
```

## Core Solution
Solution to the core problem:
Takeaway - store stuff on the object, not in the descriptor
```
UNSET = object()


class computed_property:
    def __init__(self, attr):
        self.linked_attr = attr
        self.last_linked_attr = f"_old_{self.linked_attr}"

    def __get__(self, obj, typ):
        if obj is None:
            # Attempting to __get__ on the actual class, not an object. Just return the descriptor self
            return self
        if getattr(obj, self.computed_attr, UNSET) is UNSET or getattr(
            obj, self.last_linked_attr
        ) != getattr(obj, self.linked_attr):
            setattr(obj, self.computed_attr, self.func(obj))
            setattr(obj, self.last_linked_attr, getattr(obj, self.linked_attr))
        return getattr(obj, self.computed_attr)
        #  if getattr(obj, self.computed_attr, UNSET) is UNSET:
        #      setattr(obj, self.computed_attr, self.func(obj))
        #      setattr(obj, self.last_linked_attr, getattr(obj, self.linked_attr))
        #  elif getattr(obj, self.last_linked_attr) != getattr(obj, self.linked_attr):
        #      setattr(obj, self.computed_attr, self.func(obj))
        #      setattr(obj, self.last_linked_attr, getattr(obj, self.linked_attr))
        #  return getattr(obj, self.computed_attr)

    def __set__(self, obj, value):
        raise AttributeError(f"Can't set {self.name}")

    def __call__(self, func, *args, **kwargs):
        self.func = func
        return self

    def __set_name__(self, obj, name):
        self.computed_attr = f"_{name}"
```

## Bonus 1
This bonus wasn't too bad, just made lists out of what was singular for linked_attrs
Moved the massive if statement into two functions as well which I think improves readability

```
UNSET = object()


class computed_property:
    def __init__(self, *attrs):
        self.linked_attrs = attrs
        self.last_linked_attr_mapping = {
            attr: f"_old_{attr}" for attr in self.linked_attrs
        }

    def __get__(self, obj, typ):
        if obj is None:
            # Attempting to __get__ on the actual class, not an object. Just return the descriptor self
            return self
        if self.not_yet_computed(obj) or self.linked_attrs_updated(obj):
            setattr(obj, self.computed_attr, self.func(obj))
            for attr in self.linked_attrs:
                setattr(obj, self.last_linked_attr_mapping[attr], getattr(obj, attr))
        return getattr(obj, self.computed_attr)

    def __set__(self, obj, value):
        raise AttributeError(f"Can't set {self.name}")

    def __call__(self, func, *args, **kwargs):
        self.func = func
        return self

    def __set_name__(self, obj, name):
        self.computed_attr = f"_{name}"

    def not_yet_computed(self, obj):
        return getattr(obj, self.computed_attr, UNSET) is UNSET

    def linked_attrs_updated(self, obj):
        return any(
            getattr(obj, self.last_linked_attr_mapping[attr]) != getattr(obj, attr)
            for attr in self.linked_attrs
        )
```


## Bonus 2
Bonus 2 wants us to be able to have undefined linked attributes. Easy, just stick the UNSET sentinel value in all of the `getattr` calls
```
UNSET = object()


class computed_property:
    def __init__(self, *attrs):
        self.linked_attrs = attrs
        self.last_linked_attr_mapping = {
            attr: f"_old_{attr}" for attr in self.linked_attrs
        }

    def __get__(self, obj, typ):
        if obj is None:
            # Attempting to __get__ on the actual class, not an object. Just return the descriptor self
            return self
        if self.not_yet_computed(obj) or self.linked_attrs_updated(obj):
            setattr(obj, self.computed_attr, self.func(obj))
            for attr in self.linked_attrs:
                setattr(obj, self.last_linked_attr_mapping[attr], getattr(obj, attr, UNSET))
        return getattr(obj, self.computed_attr)

    def __set__(self, obj, value):
        raise AttributeError(f"Can't set {self.name}")

    def __call__(self, func, *args, **kwargs):
        self.func = func
        return self

    def __set_name__(self, obj, name):
        self.computed_attr = f"_{name}"

    def not_yet_computed(self, obj):
        return getattr(obj, self.computed_attr, UNSET) is UNSET

    def linked_attrs_updated(self, obj):
        return any(
            getattr(obj, self.last_linked_attr_mapping[attr], UNSET) != getattr(obj, attr, UNSET)
            for attr in self.linked_attrs
        )
```

## Bonus 3
Not too bad either. Have the ability to do something like:
```
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    @computed_property('radius')
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
The computed_property setter method should work just like the property setter method:

>>> circle = Circle()
>>> circle.diameter
2
>>> circle.diameter = 3
>>> circle.radius
1.5
```

The beautiful part of this is that, everything will detect if the radius is changed by this method, so we don't have to do anything special. We just have to simply call the setter method if we have one.
Note: the `@diameter.setter` syntax here is syntatic sugar for the following
`<diameter function> = <diameter_computed_property_instance>.setter(<diameter function>)`
So we just add the `setter` function below and add some functionality to the `__set__` magic method.
The `setter` function just lets us save the defined function to `self._setter` to call later
Looking at it like this also makes it clear why `setter` needs to return `self`, which isn't necessarily intuitive with the decorator syntax.

```
UNSET = object()


class computed_property:
    def __init__(self, *attrs):
        self.linked_attrs = attrs
        self.last_linked_attr_mapping = {
            attr: f"_old_{attr}" for attr in self.linked_attrs
        }
        self._setter = None

    def __get__(self, obj, typ):
        if obj is None:
            # Attempting to __get__ on the actual class, not an object. Just return the descriptor self
            return self
        if self.not_yet_computed(obj) or self.linked_attrs_updated(obj):
            setattr(obj, self.computed_attr, self.func(obj))
            for attr in self.linked_attrs:
                setattr(
                    obj, self.last_linked_attr_mapping[attr], getattr(obj, attr, UNSET)
                )
        return getattr(obj, self.computed_attr)

    def __set__(self, obj, value):
        if not self._setter:
            raise AttributeError(f"Can't set {self.name}")
        self._setter(obj, value)

    def __call__(self, func, *args, **kwargs):
        self.func = func
        return self

    def __set_name__(self, obj, name):
        self.computed_attr = f"_{name}"

    def not_yet_computed(self, obj):
        return getattr(obj, self.computed_attr, UNSET) is UNSET

    def linked_attrs_updated(self, obj):
        return any(
            getattr(obj, self.last_linked_attr_mapping[attr], UNSET)
            != getattr(obj, attr, UNSET)
            for attr in self.linked_attrs
        )

    def setter(self, func):
        """ This function is what gets called when you do @<attributename>.setter """
        self._setter = func
        return self

```
