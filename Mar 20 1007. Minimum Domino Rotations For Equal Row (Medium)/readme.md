**[LeetCode Discuss Post](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/1867467/PythonGO-Greedy-Counter-Solution-and-Explanation)**
# [Python/GO] 🌟 Greedy Counter Solution and Explanation 💕
## 1️⃣ Main Idea:
1. A very greedy idea is to check if we can swap dice's number to make them equals to 1~6. But actually, we only have to deal with two number **tops[0] and bottoms[0]**
	* Because at maximum we only have to deal with two possible number swap, all remaining number will be invalid since we can't swap other dices to have same value besides these two number.
2. We simply loops through both tops and bottoms with two counter **swapTopCnt** and **swapBottomCnt** to store either we swap current value from top to bottom or otherwise.

## Complexity Analysis
* Time: O(N): Let N be number of element in tops' length
* Space: O(1)

## Code

**Python**
```python
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = float('inf')
        # Loops through tops[0] or bottoms[0]
        for i in (tops[0], bottoms[0]):
            isValid = True
            swapTopCnt, swapBottomCnt = 0, 0
            for top, bottom in zip(tops, bottoms):
                if top == i and bottom == i:
                    continue
                # Count if we have to  Swap Top to Bottom
                elif top == i:
                    swapTopCnt += 1
                # Count if we have to  Swap Bottom to Top
                elif bottom == i:
                    swapBottomCnt += 1
                # If not valid, don't update res
                else:
                    isValid = False
                    break
            # Check whether make all top value equal, or bottom value equal takes minimum swaps
            if isValid:
                res = min(res, swapTopCnt, swapBottomCnt)
                
        return res if res != float('inf') else -1
```
**Go** : Hope find a elegant better way to write if isValid part
```go
func minDominoRotations(tops []int, bottoms []int) int {
    res := -1
    // Loops through tops[0] or bottoms[0]
    for _, val := range([]int{tops[0], bottoms[0]}){
        isValid := true
        swapTopCnt, swapBottomCnt := 0, 0
        for idx:= 0; idx < len(tops); idx++{
            if tops[idx] == val && bottoms[idx] == val{
                continue
            // Count if we have to  Swap Top to Bottom
            } else if tops[idx] == val {
                swapTopCnt += 1
            // Count if we have to  Swap Bottom to Top
            } else if bottoms[idx] == val{
                swapBottomCnt += 1
            // If not valid, don't update res
            } else{
                isValid = false
                break
            }
        }
        // Check whether make all top value equal, or bottom value equal takes minimum swaps
        if isValid{
            if res == -1{
                res = swapTopCnt
            }
            if swapTopCnt < res{
                res = swapTopCnt
            }
            if swapBottomCnt < res{
                res = swapBottomCnt
            }
        }
    }
    
    return res
}
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
