import weakref


def instance_tracker(tracker_list_name="instances"):
    class InstanceTracker:
        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            getattr(cls, tracker_list_name).add(instance)
            return instance

    setattr(InstanceTracker, tracker_list_name, weakref.WeakSet())
    return InstanceTracker
