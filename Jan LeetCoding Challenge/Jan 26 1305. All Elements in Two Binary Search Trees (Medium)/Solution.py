# Recursive
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2 = [], []
        self.inOrder(root1, list1)
        self.inOrder(root2, list2)
        return self.mergeSortedList(list1, list2)
    
    def inOrder(self, node, res):
        if node is None: return
        self.preOrder(node.left, res)
        res.append(node.val)
        self.preOrder(node.right, res)
        
    def mergeSortedList(self, list1, list2):
        i, j = 0, 0
        res = []
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
                
        while i < len(list1):
            res.append(list1[i])
            i += 1
        while j < len(list2):
            res.append(list2[j])
            j += 1
        return res

# Iterative
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, res = [], [], []
        tree1Node = self.getNextNode(stack1, root1)
        tree2Node = self.getNextNode(stack2, root2)
        
        while tree1Node and tree2Node and len(stack1) and len(stack2):
            if tree1Node.val <= tree2Node.val:
                stack1.pop()
                res.append(tree1Node.val)
                tree1Node = self.getNextNode(stack1, tree1Node.right)
            else:
                stack2.pop()
                res.append(tree2Node.val)
                tree2Node = self.getNextNode(stack2, tree2Node.right)
        
        while tree1Node and len(stack1):
            stack1.pop()
            res.append(tree1Node.val)
            tree1Node = self.getNextNode(stack1, tree1Node.right)
            
        
        while tree2Node and len(stack2):
            stack2.pop()
            res.append(tree2Node.val)
            tree2Node = self.getNextNode(stack2, tree2Node.right)
        return res
    
    
    def getNextNode(self, stack, node):
        while node is not None:
            stack.append(node)
            node = node.left
        return stack[-1] if stack else None
  
