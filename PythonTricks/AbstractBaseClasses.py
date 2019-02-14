# Not using abc module
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    # We haven't overridden bar()

b = Base()
# Errors:
# b.foo()
c = Concrete()
c.foo()
# Errors:
#  c.bar()

# instantiating b should error, and we can successfully have an incomplete
# subclass c that doesn't error until we call c.bar()

# NOTE THE FOLLOWING NEEDS TO BE RUN WITH PYTHON3
from abc import ABCMeta, abstractmethod

class GoodBase(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class BadConcrete(GoodBase):
    def foo(self):
        pass


assert issubclass(BadConcrete, GoodBase)
# This errors because we haven't implemented bar:
# c = BadConcrete()

class GoodConcrete(GoodBase):
    def foo(self):
        pass
    def bar(self):
        pass

c = GoodConcrete()


