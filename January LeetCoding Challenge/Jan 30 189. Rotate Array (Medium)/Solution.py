# Use Auxiliary Space
# O(n) | O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        auxArr = [0] * len(nums)
        k %= len(nums)
        for i in range(len(nums)):
            auxArr[(i + k) % len(nums)] = nums[i]
        nums[:] = auxArr
# Reverse Array
# O(n) | O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverseArray(0, len(nums) - 1, nums)
        self.reverseArray(0, k - 1, nums)
        self.reverseArray(k, len(nums) - 1, nums)

    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
# Cyclic Move elements
# O(n) | O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        
        start, move = 0, 0
        while move < len(nums):
            current, prev = start, nums[start]
            while True:
                nextIdx = (current + k) % len(nums)
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                move += 1
                if current == start:
                    break
            start += 1
