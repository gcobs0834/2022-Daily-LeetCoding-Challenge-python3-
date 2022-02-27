# [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

 

## Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
## Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
## Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

# 🌟[Python 3] BFS and DFS Solutions and Explanation 💕

## 1️⃣ BFS Approach:
Because we want return maximum width of the binary tree, so we use BFS to iterate through level by level. And every time we pass its idx in that levle.
* **leftChildIdx = parentIdx * 2, rightChildIdx = parentIdx * 2 + 1**
```
# Indexed level by level
        0
      /    \
    0        1
  /  \     /   \
0    1    2      3
```

We will append child from left to right at every level, so we can make sure queue[0] and queue[-1] are left and right most node.
And once we append all child to nextLevelQueue, we then iterate nextLevelQueue to find maximum width.

## Complexity Analysis
* Time: O(N) : We use BFS to traverse whole tree.
* Space: O(N) : There are at worst N // 2 nodes at final level => O(N)
## BFS Code
```
# BFS Solution O(N) | O(N)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Each index in queue store node and its index in its level
        queue = [(root, 0)]
        maxLength = 1
        while queue:
            nextLevelQueue = []
            # Calculate leftMost and rightMost node
            leftMost, rightMost = queue[0][1], queue[-1][1]
            maxLength = max(maxLength, rightMost - leftMost + 1)
            
            # Append next level's node into new queue
            for currNode, idx in queue:
                # If left, right child exist: append it and its idx
                if currNode.left:
                    nextLevelQueue.append((currNode.left, idx * 2))
                if currNode.right:
                    nextLevelQueue.append((currNode.right, idx * 2 + 1))
            # Replace queue to nextLevelQueue
            queue = nextLevelQueue
        return maxLength

```

## 2️⃣ DFS Naive Approach:
BFS Solution may seem intuitive for this question. But we can also use DFS to solve this question as well.

1. **Init HashMap**
	* We use levelHash to store leftMost and rightMost index at certain level
	* Once we traverse through whole tree we can simply itreate through levelHash to find maximum width

2. **Make DFS Call**
	* Every time we recursive call dfs function, we also have to pass in its **index and level** to update levelHash
3. **Find max width**
	* Iterate through levelHash's values to find maximum width and return

## Complexity Analysis
* Time: O(N) :  1. We use DFS to traverse whole tree => O(N) | 2. Iterate through levelHash update maxLength => O(N). So its O(N)
* Space: O(N) : levelHash and recursive call at worst take O(N) (Skewed binary tree)
## DFS Code
```
# DFS Soultion O(N) | O(N)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Make hashMap level = [leftMost, rightMost]
        levelHash = {}
        self.dfs(root, 0, 0, levelHash)
        maxLength = 0
        for leftMost, rightMost in levelHash.values():
            maxLength = max(maxLength, rightMost - leftMost + 1)
        return maxLength
        
        
    def dfs(self, node, idx, level, levelHash):
        if node is None:
            return
        if level not in levelHash:
            # Make level = [leftMost, rightMost]
            levelHash[level] = [idx, idx]
        else:
            if idx < levelHash[level][0]:
                levelHash[level][0] = idx
            if idx > levelHash[level][1]:
                levelHash[level][1] = idx
                
        # Search left and right
        self.dfs(node.left, idx * 2, level + 1, levelHash)
        self.dfs(node.right, idx * 2 + 1, level + 1, levelHash)
```

## 3️⃣ Optimal DFS Approach:
* Since we use preorder traverse. It's guarantee that the first node we meet at its level would be leftMost. 
So we make maxLength = max(maxLength, idx - levelHash[level] + 1)

## Complexity Analysis
* Time: O(N) :  1. We use DFS to traverse whole tree => O(N) | 2. Iterate through levelHash update maxLength => O(N). So its O(N)
* Space: O(N) : Still O(N) but **only store leftMost** idx in levelHash

## DFS Optimal Code
```
# DFS Optimal Soultion O(N) | O(N)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Make hashMap level = [leftMost, rightMost]
        levelHash = {}
        maxLength = 1
        def dfs(node, idx, level):
            nonlocal maxLength
            if node is None:
                return
            # Since we search left child fist, It's guarantee that the first node we meet at its level would be leftMost
            if level not in levelHash:
                # Make level = leftMost idx
                levelHash[level] = idx
            else:
                # Update maxLength
                maxLength = max(maxLength, idx - levelHash[level] + 1)
				
            # Search left and right
            dfs(node.left, idx * 2, level + 1)
            dfs(node.right, idx * 2 + 1, level + 1)
        dfs(root, 0, 0)
        return maxLength
```
