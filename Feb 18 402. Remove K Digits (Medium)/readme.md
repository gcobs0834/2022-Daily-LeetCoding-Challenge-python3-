
# 🌟[Python 3] Greedy Stack Solution and Explanation

## 1️⃣ Greedy Approach:
* Check decription's examples "1432219" and "10200" => By observation, we can tell that every time we scan from left. We can choose to pop the larger value
```
# Example 1 k = 3
1432219 = > Check 1 and 4, pop 4
132219 = > Check 1 and 3, pop 3
12219 => Check 1 and 2, pop 2
1219
```
* But there are some edge cases we need to  check, what if first and second value **equal to each other**?
```
# Example 2 k =2
11123 => Check 1 and 1, skip (idx 0 and 1)
11123 => Check 1 and 1, skip (idx 1 and 2)
11123 => Check 1 and 2, pop 2 (idx 2 and 3)
1113 => Check 1 and 3, pop 3
```

* By these two example we can tell that only a value is greater than the other we can pop it out, else we move these two number along the nums.

## Using Stack
* A clever to solve this question is using extra space **stack** to keep track all digits from begining. We don't pop inplace because it take O(N) to delete an element in list.

> Step 1. Loop through num every time see a new num check if it is **smaller** than top of stack, if so pop stack and decrease k by 1. Finally append these digits
> Step 2. An extremely edge cases it that all digit in stack are the same like '11111'. But we still have to **delete k digits**, so we do a while loop to pop out elements
> Step 3. Deal with edge cases that digits may **start with 0** pop it out.


## Complexity Analysis
* Time: O(N) : Let N be num of digits in num. We iterate through num and stack
* Space: O(N) : Using Stack


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Feb%2018%20402.%20Remove%20K%20Digits%20(Medium)/Solution.py)

# [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

## Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
## Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
## Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
