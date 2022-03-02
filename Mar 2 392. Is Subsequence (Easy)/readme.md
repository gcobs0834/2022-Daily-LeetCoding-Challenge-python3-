# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

## Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
## Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

# [Python/Go] 🌟 3 Different Solutions and Explanation 💕

## 1️⃣ Two Pointer Approach:
We use two pointer two iterate through T
1. If current letter in T == s[s_pointer], s_pointer += 1
2. We set a early exit point once s_pointer == len(s) means we already found a subsequence
## Complexity Analysis
* Time: O(T): Let T be length of target length
* Space: O(1)
## Naive Code
**Python**
```python []
# O(T) | O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_pointer = 0
        for letter in t:
            if letter == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True
        return False
```
**Go**
```go []
// O(T) | O(1)
func isSubsequence(s string, t string) bool {
    if len(s) == 0{
        return true
    }
    S_rune, T_rune := []rune(s), []rune(t)
    s_length := len(s)
    s_pointer := 0
    
    for i := 0; i < len(T_rune); i++{
        if S_rune[s_pointer] == T_rune[i]{
            s_pointer += 1
        }
        if s_pointer == s_length{
            return true
        }
    }
    return false
}
```
## 2️⃣ Follow-Up Hashmap Approach:
**Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?**

So in these case, if we follow previous solution. Simply iterate through all s, it will take O(k * T), can we make faster not loop through all T every time?

To solve this problem, we can build a hashmap for target string that stores **letter as key** and **all letter's index as value**. And iterate through all  s1, s2, ..., sk to find if there is a subsequence in T.

**Algorithm**
1. Build hashmap for T
2. Iterate letters through S
	* For every letter, since we built a hashmap we can imediately know it's position in target by hashmap
The targetHash[letter] is a list of indexes, so we could use **binary search** to find a closest index to previous index in t.
	* If index exist in targeHash[letter] we then update t_idx.

## Complexity Analysis
* Time: O(T +k*( S * logT)):
	1. Build hashmap takes O(T)
	2. Every time loop through S take O(S) and search letter takes O(logT) => O(S * logT)
* Space: O(T): Hash map
## Follow-Up Code
**Python**
``` Python []
# O(T + S * logT) | O(T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Creat a hashtable stores letter as key and all the letter index in value as list
        # Example abaa -> {"a" : [0, 2, 3], "b" : [1]}
        targetHash = defaultdict(list)
        for idx, letter in enumerate(t):
            targetHash[letter].append(idx)
            
        # Init t_idx = -1 which will represent currentLetter's index in t 
        t_idx = -1
        for letter in s:
            # Get target idxList, and find closest idx to t_idx
            letterIdxList = targetHash[letter]
            idxInHash = bisect.bisect_right(letterIdxList, t_idx) # This line will return index in letterIdxList not in t
            
            # If idx != len(letterIdxList) means there exist a letter after t_idx
            if idxInHash != len(letterIdxList):
                t_idx = letterIdxList[idxInHash] # Update t_idx
            else:
                # If we cant find a letter equals currentLetter return False
                return False
        # Once loop through all letter in s return True
        return True
```
**Go**
```go []
// O(T + S * T) | O(T)
func isSubsequence(s string, t string) bool {
    S_rune, T_rune := []rune(s), []rune(t)
     // Creat a hashtable stores letter as key and all the letter index in value as list
     // Example abaa -> {"a" : [0, 2, 3], "b" : [1]}
    targetHash := make(map[rune][]int)
    for i:=0; i < len(T_rune); i++{
        letter := T_rune[i]
        targetHash[letter] = append(targetHash[letter], i)
    }
    // Init t_idx = -1 which will represent currentLetter's index in t
    t_idx := -1
    
    for i:=0; i < len(S_rune); i++{
        // Get target idxList, and find closest idx to t_idx
        letter := S_rune[i]
        letterIdxList := targetHash[letter]
        // Linear search in letterIdxList find idx> t_idx
        foundMatch := false
        for _ , idx := range letterIdxList{
            if idx > t_idx{
                foundMatch = true
                t_idx = idx
                break
            } 
        }
        // if not found a match return false
        if !foundMatch{
            return false   
        }
    }
    return true
}
```
## 3️⃣ DP Approach:
**It's no need to use DP solution beacuse we only check if there is a subsequence takes all letter in S not maximum subsequence**

See [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## Complexity Analysis
* Time: O(S * T)
* Space: O(S * T)

## DP Code
**Python**
``` Python []
# O(S * T) | O(S * T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        
        # Loops through dp
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                sIdx, tIdx = col - 1, row - 1
                if s[sIdx] == t[tIdx]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])     
            # Early break, once we iterate through a row if dp[row][col] == len(s) means found a subsequence
            if dp[row][col] == len(s):
                return True   
        return False
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
