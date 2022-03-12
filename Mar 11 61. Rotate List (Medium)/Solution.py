# O(N) | O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length = 1
        curr = head
        # Calculate length of linked-list
        while curr.next is not None:
            length += 1
            curr = curr.next
        curr.next = head
        
        # Calculate length before k element
        k %= length
        lengthPrev = length - k - 1
        curr = head
        # Move curr to new tail
        for _ in range(lengthPrev):
            curr = curr.next
        # New head would be tail.next
        res = curr.next
        # Make tali point to None
        curr.next = None
        
        return res
