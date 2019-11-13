# Basic solution
#  def alias(alias_string):
#      def getter(self):
#          return getattr(self, alias_string)
#      return property(getter)


class alias:

    def __init__(self, alias_string, write=False):
        self.alias_string = alias_string
        self.write = write
    
    def __get__(self, obj, objtype):
        if obj is None:
            return getattr(objtype, self.alias_string)
        return getattr(obj, self.alias_string)

    def __set__(self, obj, val):
        if not self.write:
            raise AttributeError
        setattr(obj, self.alias_string, val)
