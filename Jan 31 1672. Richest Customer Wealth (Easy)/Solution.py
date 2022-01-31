class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        currentMax = 0
        for account in accounts:
            if sum(account) > currentMax:
                currentMax = sum(account)
        return currentMax
      
# One-liner
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts )
