from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix #it changes the number in the res array to the current value of prefix
            prefix *= nums[i] #then it multiplies by the number in the original array
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix #the number in the res array multiplied by the postfix
            postfix *= nums[i] #postfix multiplied by the number in the original array
        return res