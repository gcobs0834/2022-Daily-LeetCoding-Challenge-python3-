# O(N) | O(N)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Num, l2Num = 0, 0
        idx = 1
        # calculate l1Num and l2Num
        while l1 or l2:
            if l1:
                l1Num += l1.val * idx
                l1 = l1.next
            if l2:
                l2Num += l2.val * idx
                l2 = l2.next
            idx *= 10
            
        outputNum = l1Num + l2Num
        remainder = outputNum % 10
        outputNum //= 10
        outputHead = ListNode(remainder)
        curr = outputHead
        
        # Create output linked-list
        while outputNum > 0:
            remainder = outputNum % 10
            curr.next = ListNode(remainder)
            curr = curr.next
            outputNum //= 10
        return outputHead

# O(N) | O(N)
class Solution:
    def addTwoNumbers(self, l1, l2):
        # Init dummy nodes and carry
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            # Calculate value and carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currValue = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            # Create a new node, and make curr.next point to it
            curr.next = ListNode(currValue)
            # Move curr, l1 and l2 forward
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # if carry != 0 means we have to create a new node
        if carry:
            curr.next = ListNode(carry)
            
        return dummy.next
