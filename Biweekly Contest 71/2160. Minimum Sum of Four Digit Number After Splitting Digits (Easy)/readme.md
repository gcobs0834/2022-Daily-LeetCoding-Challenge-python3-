
# [Python 3] Super Easy Solution🔎

## MAIN IDEA
Eventually we have to minimize final ouput = a*10 + b*10 + c + d  => a,b,c,d be number in nums
So we can say we need to find a, b to be two minimum digit in num

> Step 1: Covert num into 4 digit list
> Step 2: Sort nums
> Step 3: return return nums[0] * 10 + nums[1] * 10 + nums[2] + nums[3]
## Complexity Analysis
* Time : O(1) Althrough we sorted an array but there are only 4 digit in num
* Space: O(1)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Biweekly%20Contest%2071/2160.%20Minimum%20Sum%20of%20Four%20Digit%20Number%20After%20Splitting%20Digits%20(Easy)/Solution.py)

# [2160. Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)

You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

 

## Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
## Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 

Constraints:

1000 <= num <= 9999
