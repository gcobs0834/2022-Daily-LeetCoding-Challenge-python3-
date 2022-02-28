# [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/)

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

## Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
## Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.


# [Python 3] 🌟 Detailed Solution and Explanation 💕

## 1️⃣ Main Idea:
**main function**

0. Edge Case: if nums = [ ] return [ ]
1.  Init parameters
	* init final result's array res = [ ] 
	* init currRange = [startPoint, endPoint] both nums[0]
2.  Iterate through nums:
	* If current num is not consecutive to previous one, append currRange to res and reinit currRange  = [currentNum, currentNum]
	* Else we expand endPoint to current numbers, currRange[1] = nums[i]
3. Once finish iteration, append final range to result.
 
**updateSummary** function is to convert currRange to corrent format and append it to summary
1. Case 1: if startPoint == endPoint: append "a"
2. Case 2: if startPoint != endPoint append "a->b"

## Complexity Analysis
* Time: O(N) : Iterate through nums O(N)
* Space: O(1)
## Solution Code
```
# O(N) | O(1)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        # Init parameters currRange = [startPoint, endPoint]
        res = []
        currRange = [nums[0], nums[0]]
        
        for i in range(1, len(nums)):
            # Once nums are not consecutive, update res and reinit currRange
            if nums[i] != nums[i - 1] + 1:
                self.updateSummary(currRange, res)
                currRange = [nums[i], nums[i]]
            # Update endPoint
            else:
                currRange[1] = nums[i]
                
        # Update res again to append final range
        self.updateSummary(currRange, res)
        return res
    
    def updateSummary(self, currRange, summary):
        # Case 1: "a" if a == b
        if currRange[0] == currRange[1]:
            summary.append(str(currRange[0]))
        # Case 2: "a->b" if a != b
        else:
            summary.append("{}->{}".format(currRange[0], currRange[1]))
```
