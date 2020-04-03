This week I'd like you to create a Month class which represents a specific month in a specific year.

>>> dec99 = Month(1999, 12)
>>> dec99
Month(1999, 12)
>>> print(dec99)
1999-12
Month objects should have two different string representations (see above). They should also be comparable to each other using equality and ordering operators:

>>> sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)])
[Month(1998, 12), Month(1999, 12), Month(2000, 1)]
Month objects should not be comparable to tuples, lists, date objects, or other non-Month objects (just as tuples and lists are not comparable to each other).

>>> Month(1998, 12) < (1998, 12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Month' and 'tuple'
If you have time to add more features to your Month class, I have three bonuses for you.

Bonus 1

For the first bonus, I'd like your Month object to have first_day and last_day attributes which hold the datetime.date object representing the first and last days of the month:

>>> dec99 = Month(1999, 12)
>>> dec99.first_day
datetime.date(1999, 12, 1)
>>> dec99.last_day
datetime.date(1999, 12, 31)
Bonus 2

For the second bonus, I'd like your Month object to have a factory method for creating Month objects from datetime.date objects and an instance method for converting Month objects to a specific string representation (using the same strftime syntax as datetime.date objects).

>>> from datetime import date
>>> nye99 = date(1999, 12, 31)
>>> dec99 = Month.from_date(nye99)
>>> dec99
Month(1999, 12)
>>> dec99.strftime('%b %Y')
Dec 1999
Bonus 3

For the third bonus, your Month objects should be immutable, hashable, and memory efficient (you shouldn't have a __dict__ for each Month object):

>>> dec99 = Month(1999, 12)
>>> dec99.year = 1998
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> {Month(1999, 12), dec99, Month(2000, 1)}
{Month(1999, 12), Month(2000, 1)}
