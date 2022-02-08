
# [Python 3]2️⃣ Solution Iterative and Math Solution♾️


## 1️⃣ Approach 1: Iterative
* While **length** of num >1 we **sum up** all digits:
> Step 1. Convert num into digits list
> Step 2. Sum up all digits back to **while** loop

Once length of num == 1 return num

## Complexity Analysis
* Time: **O(ceil(log10(n))^2)** : Let *N* be the length of num, for we iterate through digits in num
* Space: **O(ceil(log10(n)))** : We store digits in maximum log10(n)

## Iterative Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/e523064a634f9e2b5e7346d1955f00156854d888/Feb%208%20258.%20Add%20Digits%20(Easy)/Solution.py#L2)

## 2️⃣ Approach 2: Math -> Digital Root
In Digital Root Formula [See Wikipedia](https://en.wikipedia.org/wiki/Digital_root):

1. num == 0 => **sum = 0**
2. num % 9 == 9 => **sum = 9**
3. num % 9 != 9 =>**sum = num % 9**

## Complexity Analysis
* Time: O(1)
* Space: O(1)

## Math Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/e523064a634f9e2b5e7346d1955f00156854d888/Feb%208%20258.%20Add%20Digits%20(Easy)/Solution.py#L9)


## One Linear Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/e523064a634f9e2b5e7346d1955f00156854d888/Feb%208%20258.%20Add%20Digits%20(Easy)/Solution.py#L18)

# [258. Add Digits](https://leetcode.com/problems/add-digits/)

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

## Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
## Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
