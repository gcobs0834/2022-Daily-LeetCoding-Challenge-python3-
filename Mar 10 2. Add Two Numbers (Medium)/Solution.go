func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := ListNode{0, nil}
    curr := &dummy
    carry := 0
    for l1 != nil || l2 != nil{
        // Calculate value and carry
        val1, val2 := 0, 0
        if l1 != nil{
            val1 = l1.Val
        }
        if l2 != nil{
            val2 = l2.Val
        }
        currValue := (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) / 10
        // Create a new node, and make curr.next point to it
        curr.Next = &ListNode{currValue, nil}
        // # Move curr, l1 and l2 forward
        curr = curr.Next
        if l1 != nil{
            l1 = l1.Next
        }
        if l2 != nil{
            l2 = l2.Next
        }  
    }
    // if carry != 0 means we have to create a new node
    if carry != 0{
        curr.Next = &ListNode{carry, nil}
    }
    
    return dummy.Next
}
