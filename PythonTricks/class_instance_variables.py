# Class variables and instance variables
# Modifying a class variable affects all objects of the same type
# Class variables defined outside of any instance methods
# Instance variables always tied to a specific object instance. Not stored on
# class but rather each individual object, completely independent from objects
# of the same type

class Dog:
    # Class variable
    num_legs = 4
    
    def __init__(self, name):
        # Instance variable
        self.name = name

jack = Dog("jack")
jill = Dog("jill")
print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)
print(Dog.num_legs)
# print(Dog.name) will fail
assert (jack.num_legs, jill.num_legs) == (4, 4)

Dog.num_legs = 6
print(jack.num_legs, jill.num_legs)
assert (jack.num_legs, jill.num_legs) == (6, 6)

Dog.num_legs = 4
jack.num_legs = 6
assert (jack.num_legs, jill.num_legs, Dog.num_legs) == (6, 4, 4)

# We made jack have a num_legs instance variable that shadows the class
# variable
print(jack.num_legs, jack.__class__.num_legs)
assert (jack.num_legs, jack.__class__.num_legs) == (6, 4)


# Userful example
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

        # This is BAD! it will create a shadowed instance variable named
        # num_instances
        #  self.num_instances += 1

assert CountedObject.num_instances == 0
assert CountedObject().num_instances == 1
assert CountedObject().num_instances == 2
assert CountedObject().num_instances == 3
assert CountedObject.num_instances == 3


# 4.8 Instance, Class, and Static Methods
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

# The self keyword gets you access to an objects state. You can also access the
# class itself through the self.__clas__ method

# @classmethod marks a class method, which takes a cls parameter that points to
# the class rather than a self parameter that points to the object instance
# These methods can only access the class, not individual object instances,

# static method doesn't take self or cls parameter, but can accept an arbitrary
# number of other parameters. It cannot modify object state or class tate. They
# are restricted in what data they can access, and are primarily a way to
# namespace your methods

obj = MyClass()
# Below two are the same thing. Calling method() with an object automatically
# makes itself as the first parameter
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())
print(MyClass.classmethod())
print(MyClass.staticmethod())
# This will error as expected, there is no instance to call on
#  print(MyClass.method())

# Pizza Example
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.ingredients)

    # Add class factory functions. These are factories. Note use of cls instead
    # of calling Pizza constructor directly. This allows us to not repeat
    # ourselfs,  and if we were to rename the class at some point, we wouldn't
    # have to update the contructor name in all of the factory functions
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])

p = Pizza(['cheese', 'tomatoes'])

# lots of different kinds of pizzas with different ingredients
# Give users of Pizza class better interfact by using class methods as factory
# functions

print(Pizza.margherita())
print(Pizza.prosciutto())

# These class methods sort of allow us to define alternate constructors for our
# classes. We only have one __init__ per class, so using class methods can
# essentially allow us to create however many constructors that we want


# When to use static
import math

class Pizza2:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return "{}({!r}, {!r})".format(self.__class__.__name__, self.radius, self.ingredients)

    def area(self):
        return self.circle_area(self.radius)

    # This is a way to show the method has nothing really to do with the things
    # around it. circle_area has nothing to do with pizza itself and doesn't
    # need to access the pizza object or class directly
    # This is like a flag also that this method cannot change the object. In
    # addition, it's not just a flag to other developers, it actually CANNOT
    # change anything about the object
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza2(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza2.circle_area(4))

