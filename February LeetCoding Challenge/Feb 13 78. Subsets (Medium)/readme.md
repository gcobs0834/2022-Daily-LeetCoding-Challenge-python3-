# [Python 3]  🌟 Subset Simple Solution and Explanation
## Think: How do we know that target output ?
* If we want list all of subsets we can use True or False to indicate that certain element is been chosen in the subset
``` 
#Example
 nums = [1, 2]
 output = [[], [1], [2], [1,2]]
 We can say that output could be
 [[F,F],[T,F],[F,T],[T,T]] where index 0, 1 represents number 1, 2 be selected
```

## 1️⃣ Solution Algorithm: 
In this case we can build a 
* Step 1. Init a set which contains a empty subset  ```res = [[]] ```
* Step 2. Loop through nums, each time copy original set, and add current number in
## Example
* Say we have nums = [1, 2, 3]
```
# res = []
0. res = [[]]
1. res = [[], [1]]  # Add 1 in
2. res = [[], [1] , [2], [1,2]] # Add 2 in
3. res = [[], [1] , [2], [1,2], [3], [1,3], [2,3], [1,2,3]] # Add 3 in
```

## Complexity Analysis
* Time Complexity: **O(N * 2^N)** : Since we have to put N*2^N elemet = > O(N*2^N)
* Space Complexity **O(N * 2^N)**  : Since we have to put N*2^N elemet = > O(N*2^N)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Feb%2013%2078.%20Subsets%20(Medium)/Solution.py)

# [78. Subsets](https://leetcode.com/problems/subsets/)

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

## Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
## Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
