class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by diff
        sortedCosts = sorted(costs, key = lambda x: x[0] - x[1])
        N = len(sortedCosts) // 2
        res = 0
        # Add res from both leftmost aCosts and rightmost bCosts
        for i in range(N):
            res += sortedCosts[i][0] + sortedCosts[i + N][1]
        return res
