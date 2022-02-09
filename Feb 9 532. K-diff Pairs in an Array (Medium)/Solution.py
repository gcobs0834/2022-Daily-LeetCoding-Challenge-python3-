# O(n^2)| O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftHash = {}
        
        for left in range(len(nums) - 1):
            right = left + 1
            while right < len(nums) and nums[right] - nums[left] <= k:
                if nums[right] - nums[left] == k:
                    if nums[left] not in leftHash:
                        leftHash[nums[left]] = nums[right]
                right += 1
                
        res = 0
        for left in leftHash:
            res += 1
        return res

# O(n log n)| O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        numHash = {}
        res = 0
        
        for num in nums:
            target = num - k
            if target in numHash and numHash[target]:
                res += 1
                numHash[target] = False
            if num not in numHash:
                numHash[num] = True
        return res
# O(n)| O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numsCount = {}
        
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        res = 0
        
        for key in numsCount:
            if k == 0 and numsCount[key] > 1:
                res += 1
            elif k > 0 and key + k in numsCount:
                res += 1
        return res
                
