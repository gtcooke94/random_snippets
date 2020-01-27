## Ordered Set

My approach to this was to store the data in both a set and a list. The list keeps the ordering, and the set allows for quick access and other set-like-things.

At first I tried to inherit using the `Set` class in `collections.abc`. As I was thinking about how to implement this, I realized that if I want to call the super() constructor, I will have an unordered set. I changed my mind and instead inherited from `UserList` in the `collections` module. I then called the `super().__init__()` method as the first thing in my constructor, then handled the creation of the set and the removing of duplicates from the list after that. By inheriting from `UserList`, I got indexing and `__len__` for free. I overwrote the `__contains__` method to use the `set` that the class holds for efficiency.

Adding the `add` and `discard` methods were trivial - just do the operation for the set and the list.

Adding equality such that order does not matter for comparison between an `OrderedSet` and an unordered set just compared the underlying set, whereas a comparison such that order does matter between two `OrderedSet`s just compared the underlying list instead.


After reading over the python morsel's solution, mine is terrible for one particular reason - it doesn't act like a set! We can do set operations on it. We need to inherit something to make it set like!
