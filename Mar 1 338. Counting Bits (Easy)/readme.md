# [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

## Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
## Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


# [Python/Go] 🌟 Naive and DP Solutions and Explanation 💕

## 1️⃣ Count 1s Approach:
See [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)' solution.
1. Iterate through range(n)
	* Count1s in every number from 0~n.

## Complexity Analysis
* Time: O(N logN): Iterate in range(n). each iteration takes (logN) to count 1s. 
* Space: O(N)
## Naive Code
**Python**
```python []
# Count 1s O(N logN) |O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:     
        res = [0] * (n + 1)
        for x in range(n + 1):
            res[x] = self.count1s(x)
        return res
    
    def count1s(self, n):
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count
```
**Go**
```go []
// Count 1s O(N logN) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 0; i <= n; i++{
        res[i] = count1s(i)
    }
    return res
}

func count1s(n int) int{
    count := 0
    for n != 0{
        count += 1
        n &= (n - 1)
    }
    return count
}
```
## 2️⃣ DP Approach:
By observation, we can see that every time we iterate through range(n). We can take **previous number** and **add 1** on it to indicate we add **most significant bit**.
For example 5 (0101) compares to 1 (0001) is add a **significant bit** on third digit. So that could be a DP formula.
* **DP[n] = 1 + DP[n - offset]**, where we can calculate offset is a power of 2.
## Dry Run
```
0 -> 00000
1 -> 00001 = 1 + DP[1 - 1]
2 -> 00010 = 1 + DP[2 - 2]
3 -> 00011 = 1 + DP[3 - 2]
4 -> 00100 = 1 + DP[4 - 4]
5 -> 00101 = 1 + DP[5 - 4]
6 -> 00110 = 1 + DP[6 - 4]
7 -> 00111 = 1 + DP[7 - 4]
8 -> 01000 = 1 + DP[8 - 8]
9 -> 01001 = 1 + DP[9 - 8]
```

## Complexity Analysis
* Time: O(N) : Since we not take previous number and add 1 on it. It only takes O(N)
* Space: O(N)
## DP Code
**Python**
``` Python []
# DP O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = 1 + res[i - offset]
        return res
```
**Go**
``` Go []
// DP Offset O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    offset := 1
    for i := 1; i <= n; i++{
        if offset * 2 == i{
            offset = i
        }
        res[i] = 1 + res[i - offset]
    }
    return res
}
```
## 3️⃣ DP Shift Right Approach:
This time we're not substrat by offset. But we can **divided current index by 2 to obtain left part** of least significant bit. And add **least significant bit**
* **DP[n] = (i % 2) + DP[n // 2]** or we can use **i&1** and **DP[n>>1]**
## Dry Run
```
0 -> 00000
1 -> 00001 = 1 + DP[1>>1]
2 -> 00010 = 0 + DP[2>>1]
3 -> 00011 = 1 + DP[3>>1]
4 -> 00100 = 0 + DP[4>>1]
5 -> 00101 = 1 + DP[5>>1]
6 -> 00110 = 0 + DP[6>>1]
7 -> 00111 = 1 + DP[7>>1]
8 -> 01000 = 0 + DP[8>>1]
9 -> 01001 = 1 + DP[9>>1]
```

## Complexity Analysis
* Time: O(N)
* Space: O(N)

## DP Shift Right Code
**Python**
``` Python []
# DP Shift right O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
```
**Go**
``` Go []
// DP Shift right O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 1; i <= n; i++{
        res[i] = res[i >> 1] + (i&1)
    }
    return res
}
```
Also same as [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/), We can make it **n & (n-1)**
**Python**
``` Python []
# DP Shift right O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = 1 + res[i & (i-1)]
        return res
```
**Go**
``` Go []
// DP Shift right O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 1; i <= n; i++{
        res[i] = 1 + res[i & (i-1)]
    }
    return res
}
```
