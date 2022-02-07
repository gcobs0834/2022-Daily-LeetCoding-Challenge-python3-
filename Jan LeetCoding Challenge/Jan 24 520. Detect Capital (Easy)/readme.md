# Python 3 Solution Time: O(N) Space: O(1) 
## Main Idea
Since all 3 cases will remain same cases(either lower or upper) after index 1, so we build a function call isSameCase first.
isSameCase detect if the word from left and right idx remain same case.

And then apply on 3 differnt cases
> Case 1: "USA" => If first and second char is **uppercase** then all rest are upper
> Case 2: "leetcode" = > If first and second char is **lowercase** then all rest are lowercase
> Case3 : "Google" => If first char is **uppercase** second char is **lowercase** then all rest are lowercase

## Complexity Analysis
* Time: O(n) : Let *n* be the length of the word. O(n/2) => O(N)
* Space: O(1)

# [520. Detect Capital](https://leetcode.com/problems/detect-capital/)

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

Input: word = "USA"
Output: true
# Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
