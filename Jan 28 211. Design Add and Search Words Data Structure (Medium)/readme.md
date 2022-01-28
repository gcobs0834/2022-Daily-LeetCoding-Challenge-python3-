# Python 3 Solution Trie Is All You Need Time: O(N*26^M) Space: O(M) 
## Main Idea
### addWord
> Simply build a trie

### search
> Check at every level if currentChar is '.', we recurrsive call searchHelper function on every possible leaves of currentNode, otherwise just follow method search in trie
## Complexity Analysis
### addWord
* Time: O(M) : *M* is the word length
* Space: O(M) :   In the worst-case we have to add *M* char in the trie

### search
* Time: O(N * 26^M) : *N* represents number of keys *M* is the key length
* Space: O(M) :   In the worst-case we have to use *M* stack of recurrsion stack 

## Python Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Jan%2026%201305.%20All%20Elements%20in%20Two%20Binary%20Search%20Trees%20(Medium)/Solution.py)

# [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

## Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
