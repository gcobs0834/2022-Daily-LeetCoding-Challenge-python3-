
# [Python 3]🔍Sliding Window 2 Different Solution🔎

## MAIN IDEA
We build a sliding window along big string s by using counter to count the number of each charater in the window
For example s =  "cbaebabacd", p = "abc", so the window size should be len(p) which is 3
Step1. Loop through p to count the number of every alphabet in p
Step2. Loop through s and maintain window size by pop out last element and add in new element. If sHash == pHash means we find one

> Example
```
s = "cbaebabacd"
p = "abc"
p = > a: 1, b: 1, c: 1

loop through p
1 . pHash = c: 1, b: 1, a: 1 => same as pHash
2 . pHash = b: 1, a: 1, e: 1
3 . pHash = a: 1, e: 1, b: 1
...
...
```

## 1️⃣HashMap
By using hashMap to maintain sliding window
## Complexity Analysis
* Time : O(N + M) Let *N* be the length of s and *M* be length of p.
* Space: O(1) : There are only 26 alphabet which is constant space


## Code

See [Solution.py]()

## 2️⃣Array Index Map
Instead of using hashMap, we know that alphabet letter is 1~26, so we indexed it to array and initial every index = 0 to count the number of s and p
## Complexity Analysis
* Time : O(N + M) Let *N* be the length of s and *M* be length of p.
* Space: O(1) : There are only 26 alphabet which is constant space


## Code
See [Solution.py]()

# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

## Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
## Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
