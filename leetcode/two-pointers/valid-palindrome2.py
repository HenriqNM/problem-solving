class Solution:
    def helper(self, s: str, pl: int, pr: int) -> bool:
        while pl < pr:
            if s[pl] != s[pr]:
                return False
            pl += 1
            pr -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.helper(s, l+1, r) or self.helper(s, l, r-1)
            l += 1
            r -= 1
        return True