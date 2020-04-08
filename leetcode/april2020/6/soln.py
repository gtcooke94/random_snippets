from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        to_return = []
        for word in strs:
            try:
                index = anagrams.index(Counter(word))
            except ValueError:
                index = None
            if index is not None:
                to_return[index].append(word)
            else:
                to_return.append([word])
                anagrams.append(Counter(word))
        return to_return

    def __call__(self, n):
        return self.groupAnagrams(n)
