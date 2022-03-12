**[LeetCode Post](https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1841755/pythongo-3-different-solutions-and-explanations)**
# [Python/Go] 🌟 3 Different Solutions and Explanations 💕

## 1️⃣ DFS  Approach O(N)|O(N):
1. Create a hashmap, that will render our original node to copy node.
2. DFS CALL
	* **Base Case**: If node is None return None, If node in hashMap, return its copy node
	* **Create a copy** of current node, and store it in hashMap.
	* DFS clone its next and random
	* return current node
3. return DFS(head)
## Complexity Analysis
* Time: O(N): Traverse random and next takes O(2N) => O(N)
* Space: O(N): The dfs call and graphHash both take O(N)
## DFS Code
**Python**
```python
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
```
**Go**
```go
// DFS O(N) | O(N)
func copyRandomList(head *Node) *Node {
    oldToCopy := make(map[*Node]*Node)
    var dfs func (old *Node) *Node
    dfs = func (old *Node) *Node{
        // Base Cases
        if old == nil{
            return nil 
        }
        if _, found := oldToCopy[old]; found{
            return oldToCopy[old]
        }
        // Create a copy of current node
        copyNode := Node{old.Val, nil, nil}
        oldToCopy[old] = &copyNode
        // DFS clone node's next and random
        copyNode.Next = dfs(old.Next)
        copyNode.Random = dfs(old.Random)
        
        return &copyNode
    }
    
    return dfs(head)
}
```
## 2️⃣ Iterative Approach O(N)|O(N):
1. Create a hashmap, that will render our original node to copy node.
2. Create all clone node but not connected
3. Make all connection through hashMap
## Complexity Analysis
* Time: O(N): Traverse through all nodes and create clone take O(N). Make all connection take O(N) => O(N)
* Space: O(N): The oldToCopy hashMap store O(N)
## Iterative Code
**Python**
```python
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
```
**Go**
```go
// Iterative O(N) | O(N)
func copyRandomList(head *Node) *Node {
    oldToCopy := make(map[*Node]*Node)
    oldToCopy[nil] = nil
    curr := head
    // Creat all nodes but not connected
    for curr != nil{
        copyNode := Node{curr.Val, nil, nil}
        oldToCopy[curr] = &copyNode
        curr = curr.Next
    }
    curr = head
    // Make all connection through hashMap
    for curr != nil{
        copyNode := oldToCopy[curr]
        copyNode.Next = oldToCopy[curr.Next]
        copyNode.Random = oldToCopy[curr.Random]
        curr = curr.Next
    }
    
    return oldToCopy[head]
}
```

## 3️⃣ Iterative Weaved List Approach O(N)|O(1):
Instead of a separate hashmap to keep the old node to its clone node, we can tweak the original linked list and keep every cloned node be next to its original node.
For example : ```original : A->B->C->D``` we can simpliy clone and expand the original list to ```A -> A' -> B -> B' -> C-> C' -> D -> D'``` where n' indicate its clone node.
Now we create all clone nodes, let's make all clone nodes connected to its connection
**Random**: copy.random = old.random.next
**Next**:  copy.next = copy.nex.next

**Algo**
1. Create weaved list.   ```A -> B-> C-> D``` to  ```A -> A' -> B -> B' -> C-> C' -> D -> D'```
2. Connect random.  ```copy.random = old.random.next if old.random else None```
3. Connect next and Unweaved list.
	* ```copy.next = nextOld.next if nextOld else None``` to connect clone node to its next clone node
	* ```old.next = nextOld``` to restore original connections

## Complexity Analysis
* Time: O(N):
* Space: O(N) -> O(1):
## Iterative Weaved List Code
**Python**
```python
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
```
**Go**
```go
// Iterative Weaved List O(N) | O(1)
func copyRandomList(head *Node) *Node {
    curr := head
    // Create weaved list, no connection
    for curr != nil{
        curr, curr.Next =curr.Next, &Node{Val:curr.Val, Next:curr.Next, }
    }
    
    old := head
    // Connect random
    for old != nil{
        copyNode := old.Next
        copyNode.Random = nil
        if old.Random != nil{
            copyNode.Random = old.Random.Next
        }
        old = copyNode.Next 
    }
    
    // Connect next and Unweaved list
    var newHead *Node
    if head != nil{
        newHead = head.Next
    }
    old = head
    for old != nil{
        copyNode := old.Next
        oldNext := copyNode.Next
        copyNode.Next = nil
        if oldNext != nil{
            copyNode.Next = oldNext.Next
        }
        old.Next = oldNext
        old = old.Next
    }
    return newHead
}
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
