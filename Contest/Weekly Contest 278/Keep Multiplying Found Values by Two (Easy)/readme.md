# Python 3 ✔✔ Hash Solution

## Main Idea
Step 1 . Setup numHash by looping through nums
Step 2 . orignal *= 2 until cant find orignal in numHash 
## Complexity Analysis
* Time: O(n) : Let *n* be nums's length
* Space: O(n): Hash map for nums

## Python Code
```
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numHash = {}
        for num in nums:
            if num not in numHash:
                numHash[num] = True
        while True:
            if original in numHash:
                original *= 2
            else:
                return original
```



* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)

