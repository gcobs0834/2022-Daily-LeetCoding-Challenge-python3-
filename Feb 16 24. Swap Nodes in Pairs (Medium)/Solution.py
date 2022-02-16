class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = dummy, head
        
        while current is not None and current.next is not None:
            # Save pointer
            nextPair = current.next.next
            second = current.next
            
            # Swap nodes
            second.next = current # Make second pointer point to first one
            prev.next = second # point to new head of current pair
            current.next = nextPair # point to next pair
            
            # Update pointer
            prev = current
            current = nextPair
        return dummy.next
