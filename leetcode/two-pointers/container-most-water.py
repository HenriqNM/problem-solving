class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area=0
        right=len(height)-1
        left=0
        while left<right:
            largura=right-left
            altura=min(height[left],height[right])
            calculo = altura*largura
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
            if calculo>max_area:
                max_area=calculo
        return max_area