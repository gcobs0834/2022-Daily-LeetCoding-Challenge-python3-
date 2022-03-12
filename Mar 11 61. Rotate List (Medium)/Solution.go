func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil{
        return head
    }
    
    length := 1
    curr := head
    // Calculate length of linked-list and make it circular
    for curr.Next != nil{
        length += 1
        curr = curr.Next
    }
    curr.Next = head
    // Calculate length before k element
    k %= length
    lengthPrev := length - k - 1
    curr = head
    // Move curr to new tail
    for i := 0; i < lengthPrev; i++{
        curr = curr.Next
    }
    // New head would be tail.next
    res := curr.Next
    // Make tali point to None
    curr.Next = nil
    
    return res
}
