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


"""
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
"""
