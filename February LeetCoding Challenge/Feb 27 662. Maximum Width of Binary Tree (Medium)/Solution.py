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
