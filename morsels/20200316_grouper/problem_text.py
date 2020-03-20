This week I'd like you to write a dictionary-like class that groups things. This class should accept an iterable and a key function and should group the items in the given iterable based on the result of the key function.

Here's an example of how this should work:

>>> def first_letter(word): return word[0].upper()
...
>>> sentence = 'Once upon a midnight dreary while I ponder weak and weary'
>>> groups = Grouper(sentence.split(), key=first_letter)
>>> groups['O']
['Once']
>>> groups['W']
['while', 'weak', 'weary']
>>> 'D' in groups
True
>>> 'N' in groups
False
The Grouper object should support lookups and containment checks. The initializer should also accept dictionaries in addition to other types of iterables:

>>> groups = Grouper({1: ['a'], 4: ['once', 'upon']}, key=len)
groups[1]
['a']
For the first bonus, I'd like you to make sure your Grouper object has an update method which accepts iterables of items or pre-grouped dictionaries:

>>> groups = Grouper({1: ['a'], 4: ['once', 'upon']}, key=len)
>>> groups.update({8: ['midnight'], 6: ['dreary']})
>>> groups.update(['while', 'I', 'ponder', 'weak', 'and', 'weary'])
>>> groups[4]
['once', 'upon', 'weak']
>>> groups[5]
['while', 'weary']
>>> groups[6]
['dreary', 'ponder']
For the second bonus, I'd like you to add two methods to your Grouper object: an add method and a group_for method. The add method should add a single item (figuring out which group it belongs in). The group_for method should accept a single item, figure out its group, and then return the group that item would belong in.

>>> groups = Grouper(key=len)
>>> groups.add('once')
>>> groups.group_for('upon')
4
>>> groups.group_for('a')
1
>>> groups[4]
['once']
For the third bonus, I'd like you to make every Grouper object support addition to other Grouper objects using the + operator. Using the + operator should return a new Grouper object that concatenates the groups in each of the Grouper objects:

>>> words1 = Grouper("You say goodbye and I say hello".split(), key=str.lower)
>>> words2 = Grouper("Hello hello", key=str.lower)
>>> merged = words1 + words2
>>> merged['hello']
['hello', 'Hello', 'hello']
The + operator should only work with Grouper objects that have the same key function. If two Grouper objects with different key functions are added, a ValueError should be raised.
