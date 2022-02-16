
# 🌟[Python 3] Hash Index and Sliding Window Solutions and Explanation


## 1️⃣ Main Idea:
* We combine [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)'s letter index HashMap and **Sliding Window** to solve this problem.
* We use letterHash to store **letter's index**, once we find repeated character we remove letter **from left pointer to previous occur index**, and so on.

## Complexity Analysis
* Time: O(N) : Let n be length of s => Technically it's O(2N), since we eventually may move left and right both to the end of string. But consider O(N)
* Space: O(1) : We use hashMap but it's fix length with maximum O(26) consider O(1)

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Weekly%20Premium/1100.%20Find%20K-Length%20Substrings%20With%20No%20Repeated%20Characters%20(Medium)/Solution.py)

# [1100. Find K-Length Substrings With No Repeated Characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)


Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

## Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
## Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104
