from weakref import WeakKeyDictionary
import abc

NOT_SET = object()


class Validator(abc.ABC):
    def __init__(self, default=NOT_SET):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, obj_type):
        try:
            value = getattr(obj, self.name)
        except AttributeError:
            if self.default is NOT_SET:
                raise AttributeError
            value = self.default
        return value

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.name, value)

    @abc.abstractmethod
    def validate(self, value):
        pass


class PositiveNumber(Validator):
    def validate(self, value):
        if value <= 0:
            raise ValueError()


# Original solution
#  class Validator(abc.ABC):
#      def __init__(self, default=NOT_SET):
#          self.default = default
#          self.data = WeakKeyDictionary()
#
#      def __get__(self, obj, obj_type):
#          value = self.data.get(obj, self.default)
#          if value is NOT_SET:
#              raise AttributeError
#          return value
#
#      def __set__(self, obj, value):
#          self.validate(value)
#          self.data[obj] = value
#
#      @abc.abstractmethod
#      def validate(self, value):
#          pass

# Through bonus 1
#  class PositiveNumber:
#      def __init__(self, default=NOT_SET):
#          self.default = default
#          self.data = WeakKeyDictionary()
#
#      def __get__(self, obj, obj_type):
#          value = self.data.get(obj, self.default)
#          if value is NOT_SET:
#              raise AttributeError
#          return value
#
#      def __set__(self, obj, value):
#          if value <= 0:
#              raise ValueError()
#          self.data[obj] = value
#
#
