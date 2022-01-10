# Python 3 Time: O(N) Space: O(1)
* **Main Idea**: Simply do track the carry of both number which we use len(a) and len(b) starting at last index of each number.
* In this case we can do 2^0 * a[-1] + 2^0* b[-1] +carryIn + 2^1*a[-2] + 2^1*a[-2] ...
* Time: O(N) : N depends on the longest string's length
* Space: O(1)
* In the while loop, we add up sum and carryIn and append it in the front of our output string and then substract by 1 to move to previous index

# [67. Add Binary](https://leetcode.com/problems/add-binary/)

Given two binary strings a and b, return their sum as a binary string.

 

## Example 1:

Input: a = "11", b = "1"
Output: "100"
## Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

* 1 <= a.length, b.length <= 104
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.
