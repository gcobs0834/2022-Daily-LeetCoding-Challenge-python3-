class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while fast.next and fast.next.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        return slow == fast
