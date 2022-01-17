

# Python 3 Solution Time: O(N) Space: O(1) 
## Solution 1
We build 2 hash map to store the bijection conncetion, and keep updating if the match fail return False
## Complexity Analysis
* Time: O(N) : N equals lenghth of pattern
* Space: O(N) Build 2 hashmap betten words and pattern

## Solution 2
Instead of build 2 hashmap, we build one hashmap in this solution. But use python's function **set()** to determine both pattern and words have same number of unique keys in **line 6**
## Complexity Analysis
* Time: O(N) : N equals lenghth of pattern
* Space: O(N) Build a hashmap betten words and pattern


# [290. Word Pattern](https://leetcode.com/problems/word-pattern/)

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

## Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: **true**
## Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: **false**
## Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: **false**
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
