class Solution:
    def removeElement(self, nums: list, val: int):
        nums[:] = [n for n in nums if n != val]
        return sum(1 for n in nums if isinstance(n, int))