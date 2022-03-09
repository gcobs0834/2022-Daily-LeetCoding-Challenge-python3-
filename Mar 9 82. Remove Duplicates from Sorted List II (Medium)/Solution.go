func deleteDuplicates(head *ListNode) *ListNode {
    // Create a dummy node
    dummy := ListNode{0, head}
    prev := &dummy
    
    for prev.Next != nil && prev.Next.Next != nil{
        // Init subHead
        subHead := prev.Next
        // If not duplicate move prev forward
        if subHead.Val != subHead.Next.Val{
            prev.Next = subHead
            prev = prev.Next
            continue
        }
        // If duplicate remove them and point prev.next to next integer
        // Note that we not move prev forward at this stage, only remove duplicate
        for subHead.Next != nil && subHead.Val == subHead.Next.Val{
            subHead = subHead.Next
        }
        prev.Next = subHead.Next
        
    }

    return dummy.Next
}
