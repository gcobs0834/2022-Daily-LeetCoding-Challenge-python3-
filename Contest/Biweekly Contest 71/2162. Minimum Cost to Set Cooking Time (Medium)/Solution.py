class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        buttons = []
        if targetSeconds < 100:
            buttons.append([int(c) for c in str(targetSeconds)])
            
        minTargets = targetSeconds // 60 * 100 + targetSeconds % 60
        if minTargets // 100 < 100:
            buttons.append([int(c) for c in str(minTargets)])
            
        if minTargets % 100 < 40 and minTargets > 200:
            newTarget = minTargets - 100 + 60
            buttons.append([int(c) for c in str(newTarget)])
            
        minCost = float('inf')
        
        for buttonList in buttons:
            currentCost = self.calculateCost(startAt, moveCost, pushCost, buttonList)
            minCost = min(minCost, currentCost)
        return minCost
            
            
    def calculateCost(self, startAt, moveCost, pushCost, targetButtons):
        cost = 0
        for button in targetButtons:
            if button != startAt:
                cost += moveCost
                startAt = button
            cost += pushCost
        return cost
