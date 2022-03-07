// O(N^2) | O(N^2) Recursion(Top-Down DP)
func countOrders(n int) int {
    MOD := int(math.Pow(10, 9) + 7)
    // Init cache: key = [pick, delivers] -> ways
    cache := make(map[[2]int]int)
    
    var totalWays func (picks, delivers int) int
    totalWays = func (picks, delivers int) int{
        state := [2]int{picks, delivers}
        if picks == 0 && delivers == 0{
            return 1
        }
        if picks < 0 || delivers < 0 || delivers < picks{
            return 0
        }
        // Seen in cache
        if _, found := cache[[2]int{picks, delivers}]; found{
            return cache[state]
        }
        
        res := picks * totalWays(picks - 1, delivers)
        res = res % MOD
        
        res += (delivers - picks) * totalWays(picks, delivers - 1)
        res = res % MOD
        
        cache[state] = res
        return res
    }
    
    return totalWays(n, n)
}

// O(N^2) | O(N^2) Tabulation (Bottom-UP DP)
func countOrders(n int) int {
    MOD := int(math.Pow(10, 9) + 7)
    // Init dp to be (n+1)*(n+1) array
    dp := make([][]int, n + 1)
    for i := 0; i < n + 1; i++{
        dp[i] = make([]int, n + 1)
    }
    
    for unpicked := 0; unpicked < n + 1; unpicked ++{
        for undelivered := unpicked; undelivered < n + 1; undelivered++{
            // Base case
            if unpicked == 0 && undelivered == 0{
                dp[unpicked][undelivered] = 1
                continue
            }
            
            if unpicked > 0 {
                dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] = dp[unpicked][undelivered] % MOD
            }
            
            if undelivered > unpicked{
                dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] = dp[unpicked][undelivered] % MOD
            }
        }
    }
    return dp[n][n]
}

// O(N) | O(1) Permutations (Math)
func countOrders(n int) int {
    MOD := int(math.Pow(10, 9) + 7)
    res := 1
    
    for i:=1; i < n + 1; i++{
        res = res * i
        res = res * (2 * i - 1)
        res = res % MOD
    }
    return res
}
