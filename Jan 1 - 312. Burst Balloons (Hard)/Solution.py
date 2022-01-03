class Solution(object):
    def maxCoins(self, nums):
        @cache
        def search(nums):
            return 0 if len(nums) < 3 else max([search(nums[:i + 1]) + search(nums[i:]) 
			        + nums[0] * nums[i] * nums[-1] for i in range(1, len(nums) - 1)])
        return search(tuple([1] + nums + [1]))

# Solution 2
# class Solution:
#   def maxCoins(self, nums: List[int]) -> int:
#     nums = [1] + nums + [1]
#     dp = {}
    
#     def search(l,r):
#       if l > r:
#         return 0
#       if (l,r) in dp:
#         return dp[(l,r)]
#        dp[(l,r)] = 0
#        for i in range(l,r + 1):
#         coins = nums[l-1] * nums[i] * nums[r+1]
#         coins += search(l,i-1) + search(i+1,r)
#         dp[(l,r)] = max(dp[(l,r)], coins)
#     return search(1, len(nums) - 2)
