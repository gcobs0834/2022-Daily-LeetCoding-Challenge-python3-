
# [Python 3] 🔢HashMap Solution🔢

## Main Idea
We split nums into **two part**:
**Step1**. Iterate through **first half** of nums to calculate combination of sums and add it to Hash, if we got same sum then make hash value increse by 1

**Step2** Iterate through **secnod half** to calculate if the negative complement in hash, if it is in hash we increase count by hashValue

## Complexity Analysis
* Time: O(n^2) : Let *N* be the length of nums, we iterate through first half in this case n^2
* Space: O(n^2) : Let *N* be the length of nums, since we hash first half

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Feb%203%20454.%204Sum%20II%20(Medium)/Solution.py)

# [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)


Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

## Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
## Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
