from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tracking: int = 1
        scan: int = 1

        while scan<len(nums):
            if nums[scan]!=nums[scan-1]:
                nums[tracking] = nums[scan]
                tracking += 1
            scan+=1
        return tracking