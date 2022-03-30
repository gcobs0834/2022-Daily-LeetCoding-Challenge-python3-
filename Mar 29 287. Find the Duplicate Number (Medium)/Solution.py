# Counter Set O(N) | O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = set()
        for num in nums:
            if num in counter:
                return num
            counter.add(num)
            
# Negative Marking O(N) | O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Find targetIdx
            targetIdx = abs(num) - 1
            # If already negative means duplicate
            if nums[targetIdx] < 0:
                return targetIdx + 1
            else:
                nums[targetIdx] *= -1
# Binary Search (NlogN) | O(1)     
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Count numbers <= mid
            count = sum(num <= mid for num in nums)
            if count > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        return duplicate
