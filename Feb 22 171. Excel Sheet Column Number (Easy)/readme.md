
# 🌟[Python 3] 2 Different Solutions and Explanation 💕

## 1️⃣ Scan From Right to Left Approach:
* By observation we can know that when letter from right to left increase, it immediately increase letter * 26. Just like 26 carry system but only represent by alphabet letter.
* So we can scan from right to left and each time increase carry, so we will add **(number * (26  carry))**

## Complexity Analysis
* Time: O(N) : Let N be length of columnTitle
* Space: O(1)

## Dry Run

```
columnTitle = "ABZCD"
# From right to left
Letter: D COL Num: 4 Times 1 Res = 4
Letter: C COL Num: 3 Times 26 Res = 82
Letter: Z COL Num: 26 Times 676 Res = 17658
Letter: B COL Num: 2 Times 17576 Res = 52810
Letter: A COL Num: 1 Times 456976 Res = 509786

return 509786
```

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/8b88757b7432d2ab0098c8ea6633a7eac4627b52/Feb%2022%20171.%20Excel%20Sheet%20Column%20Number%20(Easy)/Solution.py#L2)

## 2️⃣ Left to Right Approach:
* In this approach, we not scan from right. We directly scan from left, and each time res carry in, the whole res times 26.

## Dry Run

```
columnTitle = "ABZCD"
# From Left to Right
Letter: A COL Num: 1 Res = 0 * 26 + 1 = 1
Letter: B COL Num: 2 Res = 1 * 26 + 2 = 28
Letter: Z COL Num: 26 Res = 28 * 26 + 26 = 754
Letter: C COL Num: 3 Res = 754 * 26 + 3 = 19607
Letter: D COL Num: 4 Res = 19607 * 26 + 4 = 509786
```

## Complexity Analysis
* Time: O(N) : Let N be length of columnTitle
* Space: O(1)



## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/8b88757b7432d2ab0098c8ea6633a7eac4627b52/Feb%2022%20171.%20Excel%20Sheet%20Column%20Number%20(Easy)/Solution.py#L11)


# [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

## Example 1:

Input: columnTitle = "A"
Output: 1
## Example 2:

Input: columnTitle = "AB"
Output: 28
## Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
