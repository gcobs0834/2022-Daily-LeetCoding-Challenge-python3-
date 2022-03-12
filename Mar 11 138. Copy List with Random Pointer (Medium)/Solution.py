# DFS O(N) | O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashmap to tell us whether we clone this node
        oldToCopy = {} #Original -> Copy
        
        # Using dfs to traverse node, and make copy of it
        def dfs(node):
            # Base cases
            if node is None:
                return node
            if node in oldToCopy:
                return oldToCopy[node]
            # Create a copy of current node
            copyNode = Node(node.val)
            oldToCopy[node] = copyNode
            # DFS clone node's next and random
            copyNode.next = dfs(node.next)
            copyNode.random = dfs(node.random)
            
            return copyNode
        
        return dfs(head)

# Iterative O(N) | O(N)
class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None:None}
        curr = head
        # Creat all nodes but not connect
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        # Make all connection through hashMap
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        return oldToCopy[head]

# Iterative Weaved List O(N) | O(1)
class Solution:
    def copyRandomList(self, head):
        curr = head
        
        # Create weaved list, no connection
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        old = head
        
        # Connect random
        while old:
            copy = old.next
            copy.random = old.random.next if old.random else None
            old = copy.next
        cloneHead = head.next if head else None
        
        # Connect next and Unweaved list
        old = head
        while old:
            copy = old.next
            nextOld = copy.next
            copy.next = nextOld.next if nextOld else None
            old.next = nextOld
            old = old.next

        return cloneHead
        
        
        
