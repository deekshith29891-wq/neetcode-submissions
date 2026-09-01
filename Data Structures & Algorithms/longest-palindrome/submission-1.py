from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        count = sum(v//2*2 for v in c.values())
        return( count+(count<len(s)))

        