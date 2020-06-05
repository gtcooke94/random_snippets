This week I'd like you to revisit the Month class we created earlier by creating a MonthDelta class to go along with it.

You need to start with a Month class which sets year and month attributes and a MonthDelta class with a months attribute. Both should work with equality checks.

>>> m = Month(1999, 12)
>>> m.year, m.month
(1999, 12)
>>> m == Month(1999, 12)
True
>>> d = MonthDelta(5)
>>> d.months
5
>>> d == MonthDelta(5)
True
Your MonthDelta class should be addable to and subtractable from Month objects (which should return new Month objects):

>>> Month(1999, 12) + MonthDelta(5)
Month(2000, 4)
>>> Month(1999, 12) - MonthDelta(5)
And subtracting two Month objects should result in a MonthDelta:

>>> Month(2020, 1) - Month(1999, 12)
MonthDelta(241)
You'll notice that the tests also ensure your Month and MonthDelta objects should behave as expected when adding/subtracting with unknown objects (by raising a TypeError).

This problem might seem a bit odd because MonthDelta could just be an integer, but there are benefits to having a separate MonthDelta type. You might want to look at the similar datetime.timedleta object, if you haven't played with it before.

If you decide you'd like even more of a challenge, there are three bonuses this week.

Bonus 1

For the first bonus, I'd like you to allow MonthDelta objects to be added and subtracted from each other.

>>> MonthDelta(5) + MonthDelta(3)
MonthDelta(8)
>>> MonthDelta(5) - MonthDelta(3)
MonthDelta(2)
Bonus 2

For the second bonus I'd like you to make MonthDelta objects support a whole bunch of scaling, modulo, and negation operations.

Your MonthDelta objects should be:

scalable by integers with *
dividable by other MonthDelta objects with /
dividable with both MonthDelta objects and integers with //
modulo-able with both MonthDelta objects and integers
Negatable (using the unary - sign)
>>> MonthDelta(5) * 2
MonthDelta(10)
>>> -1 * MonthDelta(5)
MonthDelta(-10)
>>> MonthDelta(5) / MonthDelta(2)
2.5
>>> MonthDelta(5) // MonthDelta(2)
2
>>> MonthDelta(5) // 2
MonthDelta(2)
>>> MonthDelta(5) % 2
MonthDelta(1)
>>> MonthDelta(5) % MonthDelta(2)
1
>>> -MonthDelta(5)
MonthDelta(-5)
Bonus 3

If you finish that long second bonus, I'd like you to jump back to the Month class for the third bonus and make it support the same custom string formatting parameters that date objects do:

>>> m = Month(1999, 12)
>>> f"The year is {m:%Y} and it's a cold {m:%B} morning."
"The year is 1999 and it's a cold December morning."
>>> "We're gonna party like it's {:%b %Y}".format(m)
"We're gonna party like it's Dec 1999"
