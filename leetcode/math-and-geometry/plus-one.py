class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for n in range(len(digits)-1, -1, -1):
            if digits[n] < 9:
                digits[n]+=1
                return digits
            digits[n] = 0
        return [1] + digits