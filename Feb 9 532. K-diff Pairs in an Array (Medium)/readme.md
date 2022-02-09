
# [Python 3]3️⃣ Different Solutions and Explanation 🚩


## 1️⃣ Approach 1: Two Pointer O(n^2)
We first **sort** the array and using two pointer left and right to iterate through whole num.

We use hashmap to return the number of unique k-diff pairs

> **Left**: Iterate through nums
> **Right**: Once nums[right] - nums[left] > k, break the nested loop and move on to next left
> If nums[right] - nums[left] == k, we store leftHash[leftNum] = rightNum
> **Finally** count number of keys in the hashMap

## Complexity Analysis
* Time: O(n^2) : Let n be length of nums
* Space: O(n) : We using extra space sotre leftHash

## Two Pointer Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/1b9ef65db7e523b36afc1883e7ab2b42b6897fcb/Feb%209%20532.%20K-diff%20Pairs%20in%20an%20Array%20(Medium)/Solution.py#L2)

## 2️⃣ Approach 2: 2 Sum Solution | O(n log n)
We first **sort** the array and using 2 Sum's like method to iterate through the array

**Step 1.** Sort the array
**Step 2.** Using hashMap and iterate through nums once found target **res += 1** and set numHash[target] = **False** (To prevent duplicate counts)
## Complexity Analysis
* Time: O(n log n) : Let n be length of nums. Since we sort the array it takes (n log n)
* Space: O(n) : We using extra space sotre leftHash

## Sort and HashMap  Code

See [Soultion.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/1b9ef65db7e523b36afc1883e7ab2b42b6897fcb/Feb%209%20532.%20K-diff%20Pairs%20in%20an%20Array%20(Medium)/Solution.py#L21)


## 3️⃣ Approach 3: Count the Numbers O(n) Optimal 🦞

**Step 1.** Count the numbers in num using hashMap. =>**O(n)**
**Step 2.** Iterate through nums,
> If **k == 0** => find **numsCount** > 1
> If k > 0 => find **key + k** in **numsCount**

## Complexity Analysis
* Time: O(n) : Let n be length of nums. We iterate through nums twice => O(2N) => O(N)
* Space: O(n) : We using extra space sotre leftHash

## Counter  Code

See [Soultion.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/1b9ef65db7e523b36afc1883e7ab2b42b6897fcb/Feb%209%20532.%20K-diff%20Pairs%20in%20an%20Array%20(Medium)/Solution.py#L36)

[532. K-diff Pairs in an Array] (https://leetcode.com/problems/k-diff-pairs-in-an-array/)

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

## Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
## Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
## Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
