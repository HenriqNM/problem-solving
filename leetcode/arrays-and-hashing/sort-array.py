from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            left_arr = nums[:len(nums)//2]
            right_arr = nums[len(nums)//2:]

            self.sortArray(left_arr)
            self.sortArray(right_arr)

            left_idx = 0
            right_idx = 0
            nums_idx = 0
            while left_idx < len(left_arr) and right_idx < len(right_arr):
                if left_arr[left_idx] < right_arr[right_idx]:
                    nums[nums_idx] = left_arr[left_idx]
                    left_idx += 1
                else:
                    nums[nums_idx] = right_arr[right_idx]
                    right_idx += 1
                nums_idx += 1

            while left_idx < len(left_arr):
                nums[nums_idx] = left_arr[left_idx]
                left_idx += 1
                nums_idx += 1

            while right_idx < len(right_arr):
                nums[nums_idx] = right_arr[right_idx]
                right_idx += 1
                nums_idx += 1
        return nums