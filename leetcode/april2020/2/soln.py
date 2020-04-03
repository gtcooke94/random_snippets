class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = sum(int(i) ** 2 for i in str(n))
        return False

    def __call__(self, n):
        return self.isHappy(n)
