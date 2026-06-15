from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        scam, duplicate = 0, 0
        while scam < len(nums):
            if nums[scam] != nums[duplicate]:
