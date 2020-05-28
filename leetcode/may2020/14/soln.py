# Beat 99% of Python submissions
END_WORD = object()
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for letter in word:
            cur = cur.setdefault(letter, {})
        cur[END_WORD] = END_WORD

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for letter in word:
            try:
                cur = cur[letter]
            except KeyError:
                return False
        if END_WORD in cur:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for letter in prefix:
            try:
                cur = cur[letter]
            except KeyError:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
