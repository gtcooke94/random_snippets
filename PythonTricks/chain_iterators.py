def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i

# We can "stream" value from one iterator to another really efficiently
chain = squared(integers())
print(list(chain))

def negated(seq):
    for i in seq:
        yield -i

chain2 = negated(squared(integers()))
print(list(chain2))

# Data processing happens one element at a time, no buffering between steps in
# chain
