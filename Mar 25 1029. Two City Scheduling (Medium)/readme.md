**[LeedCode Discuss Post](https://leetcode.com/problems/two-city-scheduling/discuss/1881390/PythonGOC%2B%2B-Greedy-Solution-and-Explanations)**
# [Python/GO/C++] 🌟 Greedy Solution and Explanations 💕
## 1️⃣ Greedy Approach:
Regardless of the decription said Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
A greedy way to find minimum cost would be sorting the whole costs, and find minimum costsA or costsB.

But now we have to take care about the fact **we only allow to fly every person to a city exactly n people**.
So we can sort costs by its difference between a and b.
For example: 
```python
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

sortedCosts = [[259, 770], [184, 139], [577, 469], [926, 667], [448, 54], [840, 118]]
diff =        [-511, 45, 108, 259, 394, 722]
```
By calculating difference, we can easily find the trade off if we choose one cost instead of another. And we want minimize the tradeoff.
So we can divided the sorted cost for two part:
1. Left part would be choosing costA with least tradeoff
2. Right part would be choosing costB with least tradeoff


**Algo**
1. Sort costs by its difference.
2. Loop through costs: res += sortedCosts[i][0] + sortedCosts[i + N][1]
	
## Complexity Analysis
* Time: O(NlogN): Let N be length of costs. Sorting takes O(NlogN)
* Space: O(1): **In python, build in sorting function which uses Timsort which also has a worst-case space complexity of O(N).**

## Code

**Python**
```python
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
```
**Go**
```go
func twoCitySchedCost(costs [][]int) int {
    // Sort by diff
    sort.Slice(costs, func(i, j int) bool{
        return costs[i][0] - costs[i][1] < costs[j][0] - costs[j][1] 
    })
    
    res := 0
    N := len(costs) / 2
     // Add res from both leftmost aCosts and rightmost bCosts
    for i := 0; i < N; i++{
        res += costs[i][0] + costs[i+N][1]
    }
    return res
}
```
**C++**
```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        // Sort by diff
        sort(costs.begin(),
             costs.end(),
             [](const vector<int>&a, const vector<int>&b) { return a[0] - a[1] < b[0] - b[1];});
        
        // Add res from both leftmost aCosts and rightmost bCosts
        int res = 0, N = costs.size()/2;
        for(int i = 0; i < N; i++){
            res += costs[i][0] + costs[i + N][1];
        }
        return res;
    }
};
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
