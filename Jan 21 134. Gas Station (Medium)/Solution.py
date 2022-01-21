# class Solution:
#     Naive Approach
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
#         for i in range(len(gas)):
#             startIdx = i 
#             currentGas = gas[startIdx] - cost[startIdx]
#             startIdx = (startIdx + 1) % len(gas)
#             while startIdx != i:
#                 if currentGas < 0:
#                     break
#                 currentGas += (gas[startIdx] - cost[startIdx])
#                 startIdx = (startIdx + 1) % len(gas)
#             if currentGas >= 0:
#                 return i    
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalTank, currentTank, startStation = 0, 0, 0    
        for i in range(len(gas)):
            totalTank += (gas[i] - cost[i])
            currentTank += (gas[i] - cost[i])
            if currentTank < 0:
                startStation = i + 1
                currentTank = 0
        return startStation if totalTank >= 0 else -1
