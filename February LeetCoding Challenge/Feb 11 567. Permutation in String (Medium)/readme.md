
# [Python 3] 🍀 Two Pointer and Sliding Window Solutions and Explanation 🍀


## 1️⃣ Approach 1: # Two Pointer hashMap O(l1 + (l2 - l1) * 26 * l1)
> **Step 1.** We use hashMap or array to count **letter's frequency** from s1
> **Step 2.** By using two pointer, iterate through s2, to see if current subarray of s2 matches frequency to s1 then return True.


## Complexity Analysis
* **Time**: **O(l1 + (l2 - l1) * l1)**: Let *l1* be length of s1, *l2* be length of s2, in total it takes  O(l1 + (l2 - l1) * 26 * l1).
> **Note:** Since we copy s1Hash every time it takes O(26) and the two pointer nested loops take l1 * (l2 -l1)
* **Space**: O(1): Because number of alphabet only 26 which consider is constant space

## Two Pointer hashMap Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/b302827691b91620a4994d3cfccc7dd3a78c6e9c/Feb%2011%20567.%20Permutation%20in%20String%20(Medium)/Solution.py#L2)

## ❌2️⃣ Two Pointer Array O(l1 + (l2 - l1) * 26 * l1)
Same as previous one but we use array to map **all letter** in **different index** (From 0 ~ 25)

## Complexity Analysis
* **Time**: **O(l1 + (l2 - l1) * l1)**: Let *l1* be length of s1, *l2* be length of s2, in total it takes  O(l1 + (l2 - l1) * 26 * l1).
> **Note:** Since we copy s1Hash every time it takes O(26) and the two pointer nested loops take l1 * (l2 -l1)
* **Space**: O(1): Because number of alphabet only 26 which consider is constant space

## Two pointer Array Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/b302827691b91620a4994d3cfccc7dd3a78c6e9c/Feb%2011%20567.%20Permutation%20in%20String%20(Medium)/Solution.py#L24)



## ✔️3️⃣ Sliding Window Array O(l1 + 26 * (l2 - l1)) | O(1) 

* Instead of interate through whole length of s1, this time we only consider current window's **left and right**
* Our target is to make all s1Hash's value equals 0, since we compare s1 and current window of s2 have same frequency of letters
* Once we move window forward, we **increase** s1Hash[leftCharIdx] by 1 and **decrease** s1Hash[rightCharIdx] by 1

## Complexity Analysis
* Time: O(l1 + (l2 - l1)) : Let *l1* be length of s1, *l2* be length of s2. It takes O(l1 + 26 * (l2 - l1)) so consider to O(l1 + (l2 - l1))
* Space: O(1)

## Sliding Window Array Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/b302827691b91620a4994d3cfccc7dd3a78c6e9c/Feb%2011%20567.%20Permutation%20in%20String%20(Medium)/Solution.py#L48)


## ✔️4️⃣ Approach 4: Sliding Window Array Improved O(l1 + (l2 - l1)) | O(1) (Best) 🦞

This time we don't check if current window is match by iterate through our map.
We use a variable call match to represent it

### When moving to next window
* Left: Pop left element and if previous letter is match, then we **decrease** match by 1 and if we pop it out we matches we **increse** match by 1
* Right: Add next right element and if before we append it they matches, we need to **decrease** match by 1 and if append it make it matches : we **increse** match by 1
## Complexity Analysis
* Time: O(l1 + (l2 - l1)) : Let *l1* be length of s1, *l2* be length of s2.
* Space: O(1)

## Sliding Window Array Improved Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/b302827691b91620a4994d3cfccc7dd3a78c6e9c/Feb%2011%20567.%20Permutation%20in%20String%20(Medium)/Solution.py#L75)

# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

## Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
## Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
