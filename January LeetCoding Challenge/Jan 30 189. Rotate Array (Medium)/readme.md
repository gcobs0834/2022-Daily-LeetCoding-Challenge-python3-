
# [Python 3] 💡 3 Different Solution Explained💡

# Naive Way
## 1️⃣Use Auxiliary Space (Not Correct) O(n) Space
> By adding another auxiliary to store moved nums, and finally replace nums = auxiliary
## Complexity Analysis
* Time: O(n) : Let *n* be nums's length
* Space: O(n): Store auxiliary

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a11cff601a12daac49ec7b912a93c33c5582022d/Jan%2030%20189.%20Rotate%20Array%20(Medium)/Solution.py#L3)
# Correct Way
****Could we do it in-place with O(1) extra space?****
## 2️⃣Reverse Array
### Explanation:
> Say we have nums = [1, 2, 3, 4, 5, 6, 7], k = 3
> Step 1: Reverse nums => [7, 6, 5, 4, 3, 2, 1]
> Step 2: Reverse from 0~k and k+1~len(nums) => nums = [5, 6, 7, 1, 2, 3, 4]
> 
```
nums => [1, 2, 3, | 4, 5, 6, 7]
nums => [7, 6, 5, | 4, 3, 2, 1] reversed
nums => [5, 6, 7, | 1, 2, 3, 4] reversed sperate by index k = 3
```
## Complexity Analysis
* Time: O(n) : Let *n* be nums's length, takes twice to loop through whole array=> O(2n) = O(n)
* Space: O(1)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a11cff601a12daac49ec7b912a93c33c5582022d/Jan%2030%20189.%20Rotate%20Array%20(Medium)/Solution.py#L12)

## 3️⃣Cyclic Move elements
### Main Idea:
Eventually we have to move array's element *n* times, so we set a counter *move* = 0
> Step1. Start from index 0 => Each time we move element to index *(current + k)*, once we found our current == start, means we finished a cycle group
> Step2. Increase start by 1 => Back to step1

Explanation:
We divided nums by k groups, and each time we move one group to desire index. Once counter == len(nums) means we have moved all elements so the array is in-place moved

## Complexity Analysis
* Time: O(n) : Let *n* be nums's length
* Space: O(1)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a11cff601a12daac49ec7b912a93c33c5582022d/Jan%2030%20189.%20Rotate%20Array%20(Medium)/Solution.py#L26)

# [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

 

## Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
## Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?


