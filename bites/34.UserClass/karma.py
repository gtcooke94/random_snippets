from collections import namedtuple
from datetime import datetime

Transaction = namedtuple("Transaction", "giver points date")
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    def __init__(self, name):
        self.name = name
        self._transactions = []
        self.karma = 0
        self._fans = set()

    def __add__(self, other):
        self._transactions.append(other)
        self.karma += other.points
        self._fans.add(other.giver)

    @property
    def points(self):
        return [t.points for t in self._transactions]

    @property
    def fans(self):
        return len(self._fans)

    def __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} {'fan' if self.fans == 1 else 'fans'}"
