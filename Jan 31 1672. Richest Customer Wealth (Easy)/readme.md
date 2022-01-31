
# Python 3 👌 Super Easy Linear Time Solution

## Main Idea
Just Sum up all list inside accounts and see which one is greater
## Complexity Analysis
* Time: O(n*m) : Let *M* be the number of customers and *N* be the number of banks.
* Space: O(1)

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/1a9301f197cca38795ee8c042c627e7537ce6d33/Jan%2031%201672.%20Richest%20Customer%20Wealth%20(Easy)/Solution.py#L1)

## One-Liner
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/1a9301f197cca38795ee8c042c627e7537ce6d33/Jan%2031%201672.%20Richest%20Customer%20Wealth%20(Easy)/Solution.py#L10)

# [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

## Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
## Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
## Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
