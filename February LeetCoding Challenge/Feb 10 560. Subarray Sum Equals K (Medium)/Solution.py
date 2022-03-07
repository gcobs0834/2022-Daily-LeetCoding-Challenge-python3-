# Two Pointer Brute Force O(n^3)| O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                sumUp = 0
                for m in range(left , right + 1):
                    sumUp += nums[m]
                if sumUp == k:
                    count += 1
        return count
# Two Pointer Imporved O(n^2)| O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sumHash = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sumHash[i] = sumHash[i - 1] + nums[i - 1]
        
        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                target = sumHash[right] - sumHash[left]
                if target == k:
                    count += 1
        return count
# # HashMap O(n)| O(n) (Optimal)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sumHash = {0 : 1}
        sumUp = 0
        for i in range(len(nums)):
            sumUp += nums[i]
            count += sumHash.get(sumUp - k, 0)
            sumHash[sumUp] = sumHash.get(sumUp, 0) + 1
        return count
