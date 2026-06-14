from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for four_idx in range(n):
            if four_idx > 0 and nums[four_idx] == nums[four_idx-1]:
                continue

            for three_idx in range(four_idx+1, n):
                if three_idx > four_idx + 1 and nums[three_idx] == nums[three_idx-1]:
                    continue

                l, r = three_idx + 1, len(nums) - 1
                while l < r:
                    fourSum = nums[four_idx] + nums[three_idx] + nums[l] + nums[r]
                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        res.append([nums[four_idx], nums[three_idx], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res