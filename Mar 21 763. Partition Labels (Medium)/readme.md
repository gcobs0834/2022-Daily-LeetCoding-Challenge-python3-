**[LeetCode Discuss Post](https://leetcode.com/problems/partition-labels/discuss/1868960/pythongo-greedy-solution-and-explanation)**
# [Python/GO] 🌟 Greedy Solution and Explanation 💕
## 1️⃣ Main Idea:
A greedy way to find a valid part is to find every char's last index. And we expand current part's endIdx to the last index.

**Algo**
1. Loops through s to store every char's last index in s
2. Loops through s again. Init startIdx and endIdx, we scan every char between start and end.
	* If we found currChar's last index greater than current endIdx, means we have to expand current endIdx to the lastIdx
	* Once currIdx == endIdx, means we close a valid part so we append it into res.

## Dry Run##

```
s = "ababcbacadefegdehijhklij"
lastIdx = {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
# Starting from begining
startIdx, endIdx = 0, -1
1. At index 0 see a. The last index of a in s would be 8, so we expand endIdx = 8
2. At index 1 see b. The last index of b in s would be 5 which is less than 8. In bound
3. At index 2 see a. The last index of a in s would be 8. In bound
4. At index 3 see b. The last index of b in s would be 5. In bound
5. At index 4 see c. The last index of a in s would be 7. In bound
...
9. At index 8 see a. The last index of a in s would be 8. In bound, And we had move currIdx == endIdx
Append (8 - 0 + 1) in res
...
...
```

## Complexity Analysis
* Time: O(N): Let N be length of s. We create lastIdx take O(N) and find parts take O(N). So total O(2N) = O(N)
* Space: O(1): There are at most 26 lowercase letter in lastIdx which is constant O(1)

## Code

**Python**
```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Init lastIdx to store every char's last index in s
        lastIdx = {}
        for idx, char in enumerate(s):
            lastIdx[char] = idx
        # Init res, startIdx and endIdx
        res = []
        startIdx, endIdx = 0, -1
        # Loops through s again
        for idx, char in enumerate(s):
            # Update endIdx
            endIdx = max(lastIdx[char], endIdx)
            # If currIdx == endIdx, means we find a valid part
            # Move startIdx to next part's first index
            if idx == endIdx:
                res.append(endIdx - startIdx + 1)
                startIdx = endIdx + 1
        return res
```
**Go** : Hope find a elegant better way to write if isValid part
```go
func partitionLabels(s string) []int {
    // Init lastIdx to store every char's last index in s
    lastIdx := make(map[rune]int)
    for idx, char := range(s){
        lastIdx[char] = idx
    }
    // Init res, startIdx and endIdx
    res := make([]int, 0)
    startIdx, endIdx := 0, -1
    // Loops through s again
    for idx, char := range(s){
        // Update endIdx
        if lastIdx[char] >= endIdx{
            endIdx = lastIdx[char]
        }
        // If currIdx == endIdx, means we find a valid part
        // Move startIdx to next part's first index
        if idx == endIdx{
            res = append(res, endIdx - startIdx + 1)
            startIdx = endIdx + 1
        }
    }
    
    return res 
}
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
