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
