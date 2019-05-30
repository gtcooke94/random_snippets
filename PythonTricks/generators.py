def repeater(value):
    while True:
        yield value


gen = repeater('Hey')
# When we call the function it returns a generator object
print(gen)
# Calling next() on this object will get the next value
next(gen)

# yield essentially suspends execution of the function. The function can be
# resumed by calling next
def repeat_three_times(value):
    yield value
    yield value
    yield value

for item in repeat_three_times('hello'):
    print(item)

# Generator also stops by sending the StopIteration exception
it = repeat_three_times("Hello")
next(it)
next(it)
next(it)
# This next one will produce a StopIteration exception
# next(it)

def bounded_repeater(value, repeats):
    count = 0
    while True:
        if count >= repeats:
            return
        count += 1
        yield value
for x in bounded_repeater('Hey', 4):
    print(x)

# We can further simplify this (the return that happens is indeed a
# StopIteration exception still
# Implicit return statement at end, will raise StopIteration
def better_bounded_repeater(value, repeats):
    for i in range(repeats):
        yield value

for x in better_bounded_repeater('a', 5):
    print(x)

### Generator Expressions
iterator = ("Hello" for i in range(3))
for x in iterator:
    print(x)

# Once the generator expression has been used, it cannot be reused or
# refreshed
# They look similar to list comprehensions, however they don't construct list
# objects, instead genearting values "just in time"
# You can call list() on a generator expressions to get a list object
# containing all generator values
genexpr = ('hey' for _ in range(3))
list_gen = list(genexpr)
# Can do them in-line
for x in ('hey' for i in range(3)):
    print(x)

# Can drop the parens around them if they are the only argument to a function
print(sum((x*2 for x in range(10))))
print(sum(x*2 for x in range(10)))
