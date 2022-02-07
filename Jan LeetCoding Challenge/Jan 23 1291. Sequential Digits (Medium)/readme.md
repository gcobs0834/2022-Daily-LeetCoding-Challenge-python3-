# Python 3 Solution Time: O(N) Space: O(1) 
## Recursive Solution O(NlogN) or O(1) Space: O(1) 
Iterate through 1~9 and do recursion(DFS like) on each startNum, see if we can append sequentialDigit and stay in the boundary of both low and high.
But this need to be **sorted** in the final step so might **not be best solution**

## Complexity Analysis
* Time: O(n logn) or O(1) :  We have to sort in final step so will be n log n **BUT** In this question we only deal with **1~9 sequential number** so it is constant range
* Space: O(n) or  **O**(**1**) : We use recusion function so it grow maximum 9 recusion stack O(1)

## Recursive Code

### See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Jan%2023%201291.%20Sequential%20Digits%20(Medium)/Solution.py)

## Indexed Solution O(N) or O(1) Space: O(1) 
> Step 1. Init  sequentialDigit = '123456789'
> Step 2. Calculate the res length range and start from tens, hundreds etc. so we dont have to sort in final output.
> Step 3. Using index to find sequential number from 123456789 and within certain length
> Step4 . Repeate step2 and 3 finally retrun res

## Complexity Analysis
* Time: O(n) or O(1) : In this question we only deal with **1~9 sequential number** so it is constant range
* Space: **O**(**1**) : 

## Saved string and index solution

### See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Jan%2023%201291.%20Sequential%20Digits%20(Medium)/Solution.py)

# [1291. Sequential Digits](https://leetcode.com/problems/sequential-digits/)

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

## Example 1:

Input: low = 100, high = 300
Output: [123,234]
## Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
