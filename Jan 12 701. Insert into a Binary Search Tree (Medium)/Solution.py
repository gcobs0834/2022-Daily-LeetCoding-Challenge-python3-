class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node, parent = root, None
        
        if node is None: # In the corner case root = []
            return TreeNode(val)
        
        while node is not None: # Traverse right posistion for the val by Binary Search Tree's rules
            if val <= node.val: 
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
            
        if val <= parent.val : # Finally insert in either left or right by val
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
            
        return root
