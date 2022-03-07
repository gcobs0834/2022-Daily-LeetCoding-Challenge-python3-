
# [Python 3] 2️⃣ Easy Different Solutions and Explanation😋


## 1️⃣ Approach 1: Recursion
We use recursion to traverse the tree, and each time increse by one when we move to next level.

## Complexity Analysis
* Time: O(N) : Let n be length of nums
* Space: O(N) : Let n be number of nodes

## Recursion Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/093dfda394b5b5f8d90f3ae71c2b90fb5b81fd39/Feb%2014%20104.%20Maximum%20Depth%20of%20Binary%20Tree%20(Easy)/Solution.py#L2)

## 2️⃣ Approach 2: Iteration BFS
We use BFS to traverse whole tree, and update the maximumLevel.
## Complexity Analysis
* Time: O(N) : Let n be number of nodes
* Space: O(N): Let n be number of nodes
## Iteration Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/093dfda394b5b5f8d90f3ae71c2b90fb5b81fd39/Feb%2014%20104.%20Maximum%20Depth%20of%20Binary%20Tree%20(Easy)/Solution.py#L13)

# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

## Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
## Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
