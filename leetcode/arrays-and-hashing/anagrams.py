from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = s.lower()
        w2 = t.lower()
        if len(w1) != len(w2):
            return False
        return Counter(w1) == Counter(w2)