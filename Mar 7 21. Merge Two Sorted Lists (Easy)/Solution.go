func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // Create a dummy node to keep track of head
    dummy := ListNode{}
    curr := &dummy
    // Iterate through list1 and list2
    for list1 !=nil && list2 != nil{
        if list1.Val < list2.Val{
            curr.Next = list1
            list1 = list1.Next
        } else{
            curr.Next = list2
            list2 = list2.Next
        }
        curr = curr.Next
    }
    // For remaining
    if list1 != nil {
        curr.Next = list1
    }
    if list2 != nil {
        curr.Next = list2
    }
    
    return dummy.Next
    
}
