# O(N^2) | O(1) NAIVE
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        for start in range(len(nums)):
            count = 1 if nums[start] == 1 else -1
            for j in range(start + 1, len(nums)):
                count += 1 if nums[j] == 1 else -1
                if count == 0:
                    res = max(res, j - start + 1)
        return res
 
# O(N) | O(N) OPTIMAL
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res, count = 0, 0
        hashCount = {0: -1}
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in hashCount:
                res = max(res, i - hashCount[count])
            else:
                hashCount[count] = i
        return res
