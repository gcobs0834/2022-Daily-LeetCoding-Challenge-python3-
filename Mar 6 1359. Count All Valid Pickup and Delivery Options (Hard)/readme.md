# [1359. Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

## Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
## Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
## Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500

# [Python/Go] 🌟 3 Different Solutions and Explanation 💕

## 1️⃣ Recursion(Top-Down DP) Approach:
In a dp solution, we use pickups and deliverys as a state of dp:
1. Base Case: Both pickups and deliverys are **zero** => return 1
	* If pickups or deliverys < 0 => out of bound return 0
	* If delivers < pickups =>**Not valid sequence** : return 0
2. Recursive call two way
	1. res += Pickuped 1 order -> We could choose any order, so res = picks * totalWays(picks - 1, delivers)
	2. res += Delivered 1 order -> We only deliver pickuped order, res += (delivers - picks) * totalWays(picks, delivers - 1)
	3. **Since the answer may be too large, return it modulo 10^9 + 7.** 
3. Return totalWays(n, n)
## Complexity Analysis
* Time: O(N^2): Since we use cache memorization, we remember each state in cache to avoid repeated operation, making time complexity from **O(2^N) to O(N^2)**

* Space: O(N^2): The cache memorize **every state** (both pickups and delivers in range from 0 to N) => O((N+1) * (N+1)) = O(N^2)
## Recursion(Top-Down DP) Code
**Python**
```python []
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
```
**Go**
```go []
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
```
## 2️⃣ Tabulation (Bottom-UP DP) Approach:
0. Init DP to be a (n+1)* (n+1) array, where **rows** represent unpicked orders and **columns** represent undelivered orders
1. Base Case:Both pickups and deliverys are zero => dp[0][0] = 1
2. Take previous computation:
	*  Pickuped 1 order -> We could choose any order, so **dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]**
	*  Delivered 1 order -> We only deliver **pickuped order**(undelivered > unpicked), so **dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]**
	*  Since the answer may be too large, return it modulo 10^9 + 7.
3. Return dp[n][n]
## Complexity Analysis
* Time: O(N^2): The dp tabulation is O((N+1) * (N+1)) = O(N^2)
* Space: O(N^2): The dp tabulation is O((N+1) * (N+1)) = O(N^2)
## Tabulation (Bottom-UP DP) Code
**Python**
``` Python []
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
```
**Go**
```go []
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
```
## 3️⃣🦞 Optimal🦞 Permutations (Math) Approach:
By following math permutations:
1. We could pick orders **in any order** -> Pickups = n!
2. We only delivered orders when it is picked, -> Delivers = 1 * 3 * 5 * ... * (2n - 1)

## Delivered Explanation

```
Say we place picked in P2, P3, P4, P1, now we could arrange Delivers
Consider D1 => D1 will only deliver after P1 that is P2, P3, P4, P1, __ Only 1 slot is valid
	We place D1 in it => P2, P3, P4, P1, D1
Consider D4 => D4 will only deliver after P4 that is P2, P3, P4 __ P1 __ D1 __ There 3 slots are valid
	We now place D4 in it P2, P3, P4, P1, D1, D4
Consider D3 => D3 will only deliver after P3 that is P2, P3 __ P4 __ P1 __ D1 __ D4 __ There 5 slots are valid
	We now place D4 in it P2, P3, D3, P4, P1, D1, D4
Consider D2=> D2 will only deliver after P2 that is P2 __ P3 __ D3 __ P4 __ P1 __ D1 __ D4 __ There 7 slots are valid

So the total possible ways is 1*3*5*7
```
## Complexity Analysis
* Time: O(N)
* Space: O(1)

## Permutations (Math) Code
**Python**
```
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
```
**Go**
```go []
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
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
