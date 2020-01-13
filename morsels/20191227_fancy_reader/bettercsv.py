from collections import namedtuple
from csv import reader


class FancyReader:
    def __init__(self, lines, fieldnames=None):
        self.line_num = 0
        self.lines = reader(lines)
        if not fieldnames:
            self.line_num += 1
            fieldnames = next(self.lines)
        self.row = namedtuple("Row", fieldnames)

    def __iter__(self):
        return self

    def __next__(self):
        self.line_num += 1
        return self.row(*next(self.lines))


#  def FancyReader(lines, fieldnames=None):
#      lines = reader(lines)
#      if not fieldnames:
#          fieldnames = next(lines)
#      row = namedtuple("Row", fieldnames)
#      for line in lines:
#          yield row(*line)
