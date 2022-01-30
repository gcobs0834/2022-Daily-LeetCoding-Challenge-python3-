
# Python 3 ✔✔ Linear Time Solution

## Main Idea
Step 1.  Expand from **left to right** to calculate **0**s
Step 2.  Expand from **right to left** to calculate **1**s
Step 3.  Calculate Sum of zeroFromLeft and oneFromRight and return where maximum value's index
## Complexity Analysis
* Time: O(n) : Let *n* be nums's length
* Space: O(n): Store zeroFromLeft and oneFromRight take O(n)


## Code
```
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroFromLeft = [0] * (len(nums) + 1)
        oneFromRight = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroFromLeft[i + 1] = zeroFromLeft[i] + 1
            else:
                zeroFromLeft[i + 1] = zeroFromLeft[i]
                
        for i in range(len(nums))[::-1]:
            if nums[i] == 1:
                oneFromRight[i] = oneFromRight[i + 1] + 1
            else:
                oneFromRight[i] = oneFromRight[i + 1]
        
        allSum = [0] * (len(nums) + 1)
        currentMax = 0
        res = []
        for i in range(len(nums) + 1):
            allSum[i] = oneFromRight[i] + zeroFromLeft[i]
            if allSum[i] > currentMax:
                res = []
                currentMax = allSum[i]
            if allSum[i] == currentMax:
                res.append(i)
        return res
            
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)

