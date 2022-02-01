# O(n^2) | O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                currentMax = max(currentMax, prices[j] - prices[i])
        return currentMax
# O(n) | O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        previousLow = prices[0]
        for i in range(1, len(prices)):
            currentMax = max(currentMax, prices[i] - previousLow)
            previousLow = min(previousLow, prices[i])         
        return currentMax
        
        
