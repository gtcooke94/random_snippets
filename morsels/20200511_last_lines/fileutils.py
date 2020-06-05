# Easy  one-liner for if whole file fits in memory
def last_lines(filename):
    yield from reversed(open(filename, "r").readlines())
    #  with open(filename, "r") as f:
    #      lines = f.readlines()
    #      yield from reversed(lines)

