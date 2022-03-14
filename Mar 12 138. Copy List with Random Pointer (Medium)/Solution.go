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
