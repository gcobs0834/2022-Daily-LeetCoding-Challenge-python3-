class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node
        dummy = ListNode(-1, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Init subHead
            subHead = prev.next
            # If not duplicate move prev forward
            if subHead.val != subHead.next.val:
                prev.next = subHead
                prev = prev.next
                continue
            # If duplicate remove them and point prev.next to next integer
            # Note that we not move prev forward at this stage, only remove duplicate
            while subHead.next and subHead.val == subHead.next.val:
                subHead = subHead.next
            prev.next = subHead.next
        # return head
        return dummy.next
