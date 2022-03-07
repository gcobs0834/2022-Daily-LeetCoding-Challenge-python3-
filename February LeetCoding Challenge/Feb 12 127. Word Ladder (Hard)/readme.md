# [Python 3]  🔎🔍 Breadth First Search Solution and Explanation

### In order to solve this question we have put  hashMap and BFS together to save time we will explained it below. You can see by using hashMap we improved time complexity from O(M * N^2) to O(M^2 *N)


## ❌ 1️⃣ Approach 1: Just BFS (TLE)❌
* We use BFS to find all possible transformation and keep track with level to find shortest sequence
### In BFS Queue
> Step 1. We naive search every other element in wordList
 O(N)
>Step 2. Every time we see a new word. First check if it is visited, and we compare two words **letter by letter** and count different and put it in the queue if it's valid
O(M)
## Complexity Analysis
* Time Complexity: **O(M * N^2)**, where M is the length of each word and N is the total number of words in the input word list.
> Because we have traverse through queue take O(N) and in the queue we search every word in wordList O(N) and compare letter by letter takes O(M) => **O(M * N^2)**
* Space: O(M * N) : Queue will at worst store every element in wordList
## BFS Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/c867d535f245d8af171947db50d887c8556e205c/Feb%2012%20127.%20Word%20Ladder%20(Hard)/Solution.py#L2)

## ✔️ 2️⃣ Improved Approach : Using HashMap ✔️
* This time we dont traverse through wordList and compare letter by letter.
* We build a hashMap, whichs key store 'a*c', '*bc' for example, we use '*' sign to indicate that we can take transformation in that key and store as lists 
* So in the buildHash function we build a wordHash, which store every possible transformation

## Complexity Analysis
* Time Complexity: **O(M ^2 * N)**, where M is the length of each word and N is the total number of words in the input word list.
> We build hashMap iterate through wordList O(N) and each time we use iterate through length of word and addup '*', prefix and suffix takes O(M^2) => **O(M^2*N)**
> In breadth first search, we still at worst traverse through all element in wordList O(N), and iterate through popWord, and build the key of hashMap same as before take O(M^2) = > **O(M^2*N)**
* Space Complexity **O(M^2*N)** : O(M^2 *N) + O(M * N) + O(M * N)= O(M^2*N)


## Using HashMap Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/c867d535f245d8af171947db50d887c8556e205c/Feb%2012%20127.%20Word%20Ladder%20(Hard)/Solution.py#L37)

# [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

## Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
## Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
