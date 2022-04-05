# Brute Force O(N^2)| O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                length = right - left
                waterHeight = min(height[left], height[right])
                maxWater = max(maxWater, waterHeight * length)
        return maxWater
    
# Two Pointer O(N) | O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
