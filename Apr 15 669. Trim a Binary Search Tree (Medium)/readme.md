**[Leetcode Disscuss Post](https://leetcode.com/problems/trim-a-binary-search-tree/discuss/1948345/Python-Iterative-and-BFS-Solution-and-Explanation)**
# [Python] 🌟 Iterative and BFS Solution and Explanation 💕
## 1️⃣ Main Idea:
1. Create a dummy root, since the original root itself could be out ou bound. So we init a dummyRoot and return dummyRoot.left
2. Use BFS/DFS to traverse the tree.
	* Call **searchNextNode** function to find and connect nextValid node in both left and right child.
	* Push next left and right child into queue.
3. Return dummy.left

## Complexity Analysis
* Time: O(N) : Traverse the whole tree take O(N)
* Space: O(N) : The BFS at worst had O(N/2) nodes so => O(N)

## Code

**Python**
```python
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
```
