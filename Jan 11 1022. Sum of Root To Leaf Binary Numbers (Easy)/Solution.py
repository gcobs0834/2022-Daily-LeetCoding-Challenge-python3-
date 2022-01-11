# Recurrsion

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sumUp = 0
        self.preOrderTraverse(root, "")
        return self.sumUp
    
    def preOrderTraverse(self, node, currentNum): # CLR
        if node is None:
            return
        
        currentNum += str(node.val)
        
        if node.left is None and node.right is None: #Mean it's a leaf node
            self.sumUp += int(currentNum, 2) # Change currentNum from string type of binary digits to int and add up
            return  
        self.preOrderTraverse(node.left, currentNum)
        self.preOrderTraverse(node.right, currentNum)
        
