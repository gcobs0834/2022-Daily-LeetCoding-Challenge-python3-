# O(N^2) | O(N^2) Recursion(Top-Down DP)
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        @cache
        def totalWays(picks, delivers):
            # Base Case
            if not picks and not delivers:
                return 1
            if picks < 0 or delivers < 0 or delivers < picks:
                return 0
            
            res = picks * totalWays(picks - 1, delivers)
            res %= MOD
            
            res += (delivers - picks) * totalWays(picks, delivers - 1)
            res %= MOD
            
            return res
        
        return totalWays(n, n)

# O(N^2) | O(N^2) Tabulation (Bottom-UP DP)
class Solution:
    def countOrders(self, n):
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        return dp[n][n]

# O(N) | O(1) Permutations (Math)
class Solution:
    def countOrders(self, n):
        MOD = 1_000_000_007
        res = 1
        for i in range(1, n + 1):
            res *= i
            res %= MOD
            res *= (2 * i - 1)
            res %= MOD
        return res
