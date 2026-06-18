from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        counter1, counter2 = 0, 0
        for num in nums:
            if num == candidate1:
                counter1+=1
            elif num == candidate2:
                counter2+=1
            elif counter1 == 0:
                candidate1 = num
                counter1 = 1
            elif counter2 == 0:
                candidate2 = num
                counter2 = 1
            else:
                counter1-=1
                counter2-=1

        result = []
        if nums.count(candidate1) > len(nums)//3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > len(nums)//3:
            result.append(candidate2)

        return result