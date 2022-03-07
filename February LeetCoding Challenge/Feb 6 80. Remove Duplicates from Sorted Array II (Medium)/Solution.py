class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, count = 1, 1
        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                count +=1
            else:
                count = 1
            if count <= 2:
                nums[left] = nums[right]
                left += 1
        return left
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for idx, val in enumerate(nums):
            if (length <= 1) or (nums[length - 2] != val):
                nums[length] = val
                length += 1
        return length
