class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Creat a dummy root we return dummy.left
        dummyRoot = TreeNode(0, root)
        node = dummyRoot
        queue = deque([node])
        # BFS queue And reconstruct the tree
        while queue:
            currNode = queue.popleft()
            currNode.left = self.searchNextNode(currNode.left, low, high)
            currNode.right = self.searchNextNode(currNode.right, low, high)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        return dummyRoot.left
    
    # Find nextNode which low < node.val < high
    def searchNextNode(self, node, low, high):
        while node and (node.val < low or node.val > high):
            while node and node.val < low:
                node = node.right
            while node and node.val > high:
                node = node.left
        return node
