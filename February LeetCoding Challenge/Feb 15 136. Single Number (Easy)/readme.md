
# 🌟[Python 3] 2️⃣ Easy Different Solutions and Explanation


## 1️⃣ Approach 1: Hash Table
Since we have to count all number in the list, a naive way is use hashTable to **count all numbers** in the list
After count all number iterate through hash table to **find the key with value 1** (Appear only once)
## Complexity Analysis
* Time: O(N) : Let n be length of nums
* Space: O(N) : Let n be length of nums

## Hash Table Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/922e3db6ff7747798ef00c892a1b2eb40d1eaf56/Feb%2015%20136.%20Single%20Number%20(Easy)/Solution.py#L2)

## 2️⃣ Approach 2: XOR Operation

* ```Every element appears twice except for one.```

That's a big hint to use XOR Operation, beacuse when we use xor on same number it returns 0, after iterate through all nums and do xor operation, the remaining num is our target.

### Explanation
```
a = 7
b = 5
7    = 1 1 1 # In binary
5    = 1 0 1 # In binary
a^a  = 0 0 0
0^b  = 1 0 1 # b
return b
```

## Complexity Analysis
* Time: O(N) : Let n be length of nums
* Space: O(1)
* 
## XOR Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/922e3db6ff7747798ef00c892a1b2eb40d1eaf56/Feb%2015%20136.%20Single%20Number%20(Easy)/Solution.py#L13)


# [136. Single Number](https://leetcode.com/problems/single-number/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

## Example 1:

Input: nums = [2,2,1]
Output: 1
## Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
## Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

