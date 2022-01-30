
# Python 3 👌 HashMap Linear Time Solution

## Main Idea
We build a hashmap that stores **distances** as key and append same distances' string into same key.

Exapmple : abc -> where ord(b) - ord(a) = 1 and ord(c) - ord(b) = 1
So we store in hash[1:1] = ["abc"]
By applying this formula bcd, xyz also be [1:1] and would be append in same list

Finally we loop through all items store in hashMap and return result

## Complexity Analysis
* Time: O(n*m) : Let *n* be array's length and *m* be length of strings
* Space: O(n*m): Let *n* be array's length and *m* be length of strings

## Code
see [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Weekly%20Premium/249.%20Group%20Shifted%20Strings%20(Medium)/Solution.py)

# [249. Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/)

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

## Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
## Example 2:

Input: strings = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
