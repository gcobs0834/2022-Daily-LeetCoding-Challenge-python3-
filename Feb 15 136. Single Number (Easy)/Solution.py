# Hash Table O(N) | O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsHash = {}
        for num in nums:
            numsHash[num] = numsHash.get(num, 0 ) + 1
        
        for key, value in numsHash.items():
            if value == 1:
                return key

# XOR Operation O(N) | O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num 
        return res
