# [Python 3] 🔢HashMap Solution🔢

## Brute Force (TLE)👶
Using two nested loop to iterate through every possible subarray and count 1s and 0s once equals 0 update res
💪
## Complexity Analysis
* Time: O(n^2) : Let *N* be the length of nums
* Space: O(1) 

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/0ff771af143f3f869bab8e207ed1b3f360d06af4/Feb%204%20525.%20Contiguous%20Array%20(Medium)/Solution.py#L2)
## 💪HashMap (Optimal)💪
> Count : We update count increase by 1 if nums[i] == 1 else -1
> Hash : We store count and first calculate count number's index in hash.

## Explained
Once we see equal count number in hash, that means between these two number we have **balanced** 0s and 1s

Example:
```
index = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
nums = 1, 1, 0, 1, 1, 0, 1, 0, 0, 1
hash = -1, 0, -1,0,1, 0, 1, 0, -1,0
```

We can see above example we have -1 in index[0, 8] and 0 in index[1, 9], we can see both could be max length of Contiguous Array
## Complexity Analysis
* Time: O(n) : Let *N* be the length of nums
* Space: O(n): In worst case, we have to store every count number and index
```
# Worst Case
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
hash = {0: -1, 1: 1, 2:2 ...}
```

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/0ff771af143f3f869bab8e207ed1b3f360d06af4/Feb%204%20525.%20Contiguous%20Array%20(Medium)/Solution.py#L14)


# [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

## Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
## Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
