import math
from typing import List

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

class Solution:
    def problemname(self, nums: List[int]) -> int:
        pass


    def __call__(self, n):
        return self.problemname(n)
