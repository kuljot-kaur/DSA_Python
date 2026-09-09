class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxa = 0
        while left < right:
            width = right - left 
            ca = width * min(height[left], height[right])
            maxa = max(maxa, ca)
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return maxa