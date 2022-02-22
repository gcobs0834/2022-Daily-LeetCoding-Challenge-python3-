
# 🌟[Python 3] 2 Different Solutions and Explanation 💕

## 1️⃣ Naive Approach:
* A naive approach is to iterate through arr, once found idx == arr[idx] return.
## Complexity Analysis
* Time: O(N) : Let N be length of arr
* Space: O(1)

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/59dc69059df06b33eeda4392ff32d28692b05591/Weekly%20Premium/1064.%20Fixed%20Point%20(Easy)/Solution.py#L2)

## 2️⃣ Binary Search Approach:
* Using Binary Search to find certain index
* If we found, by problem's description: **return the smallest index i that satisfies arr[i] == i**. We need to search left part to find minimum index

## Complexity Analysis
* Time: O(log N) : Let N be length of arr
* Space: O(1)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/59dc69059df06b33eeda4392ff32d28692b05591/Weekly%20Premium/1064.%20Fixed%20Point%20(Easy)/Solution.py#L10)

# [1064. Fixed Point](https://leetcode.com/problems/fixed-point/)

Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.

 

## Example 1:

Input: arr = [-10,-5,0,3,7]
Output: 3
Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.
## Example 2:

Input: arr = [0,2,5,8,17]
Output: 0
Explanation: arr[0] = 0, thus the output is 0.
## Example 3:

Input: arr = [-10,-5,3,4,7,9]
Output: -1
Explanation: There is no such i that arr[i] == i, thus the output is -1.
 

Constraints:

1 <= arr.length < 104
-109 <= arr[i] <= 109
 

Follow up: The O(n) solution is very straightforward. Can we do better?
