
# [Python 3]3️⃣ Different Solutions and Explanation 🚩


## ❌1️⃣ Approach 1: Two Pointer Brute Force O(n^3)| O(1) 👶 (TLE)

In very naive solution will be using three nested loops.
We use left and right pointer generate every possible subarray in nums, and count the sum of subarray if equals k

## Complexity Analysis
* Time: O(n^3) : Let n be length of nums
* Space: O(1)

## Two Pointer Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/2bba4e751dbd9862b3e328672a7517e5f69e461f/Feb%2010%20560.%20Subarray%20Sum%20Equals%20K%20(Medium)/Solution.py#L2)

## ❌2️⃣ Two Pointer Improved O(n^2)| O(n) 👶 (TLE)
We can imporve previous solution by store the sum from **index 0 to end **of the nums in **sumHash**

Once we want calculate sum from **left pointer to right pointer**, we can simply use ( **sumHash[right] - sumHash[left]** ) to get the **subarray's sum**
## Complexity Analysis
* Time: O(n^2) : Let n be length of nums
* Space: O(n) : We using extra space store sumHash

## Two Pointer Improved  Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/2bba4e751dbd9862b3e328672a7517e5f69e461f/Feb%2010%20560.%20Subarray%20Sum%20Equals%20K%20(Medium)/Solution.py#L14)


## ✔️3️⃣ Approach 3: HashMap O(n)| O(n) (Optimal) 🦞
This is optimal solution since we only iterate through nums once.

> Step 1: Init sumHash = {0:1} where every **key** in hashMap indicate **sum from index 0 to current index**
>  **Value** of hashMap is **counting times** the sum number in previous nums.
>  Step 2: Iterate through nums and sum up accumulative numbers, Once we found **currentSum - k** in hashmap, means there is a subarray from the target to currrent index and add up count

* NOTE: Since we want return count to the subarray, we don't have to worry about which index form the subarray. We only care how many times a certain sum in previous we store in hashMap.

## Complexity Analysis
* Time: O(n) : Let n be length of nums.
* Space: O(n) : We using extra space store sumHash

## hashMap Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/2bba4e751dbd9862b3e328672a7517e5f69e461f/Feb%2010%20560.%20Subarray%20Sum%20Equals%20K%20(Medium)/Solution.py#L28)

# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

## Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
## Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
