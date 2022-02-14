# Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return  0
        leftLevel = 1 + self.maxDepth(root.left)
        rightLevel = 1 + self.maxDepth(root.right)
        
        return max(leftLevel, rightLevel)
        
        
# Iteration
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([[root, 1]])
        maximumLevel = 0
        while queue:
            node, level = queue.popleft()
            maximumLevel = max(maximumLevel, level)
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
        return maximumLevel
