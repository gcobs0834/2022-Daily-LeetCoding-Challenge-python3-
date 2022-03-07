
# 🌟[Python 3] DFS Recursion Solution and Explanation

## 1️⃣ Main Idea:
* Step 1. Sort candidates
* Step 2. Recurssive call our helper function

### Helper Function
* We take currentList as one of our function's input because every time we try to add in a new number from candidates
* Once we append in new number, we recurssive call helper function and this time make our target = target - num which we picked
* Also we use startIdx to prevent counting duplicated outputs

## Complexity Analysis
* Time: O(N^T/M) : Let N be length of candidates, T be target value, M be minimum value along candidates 
* Space: O(N^T/M : Let N be length of candidates, T be target value, M be minimum value along candidates

> Because every time we may at worst expand N-way tree from certain point. But how do we know the tree's **height**?
> For example: We have a smallest value 1, and target value 100. So at worst we will have a maximum height which is [1,1,1,...,1] total **100** length. So we can consider **T/M**

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Feb%2017%2039.%20Combination%20Sum%20(Medium)/Solution.py)

# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

## Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
## Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
## Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
