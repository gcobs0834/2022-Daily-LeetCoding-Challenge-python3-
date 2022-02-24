# O (nlogn) | O(logn)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        leftEnd = self.getMidNode(head)
        
        right = leftEnd.next
        leftEnd.next = None
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeList(left, right)
    
    def getMidNode(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        
    def mergeList(self, node1, node2):
        dummy = ListNode(0)
        currNode = dummy
        while node1 and node2:
            if node1.val < node2.val:
                currNode.next = node1
                node1 = node1.next
            else:
                currNode.next = node2
                node2 = node2.next
            currNode = currNode.next
        if node1:
            currNode.next = node1
        if node2:
            currNode.next = node2
        return dummy.next


# O (nlogn) | O(1)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
             return head
            
        totalLength = self.countLengthOfList(head)
        currLength = 1
        dummyHead = ListNode(0)
        dummyHead.next = head
        while currLength < totalLength:
            list1 = dummyHead.next
            prevTail = dummyHead
            while list1:
                prevTail.next = list1
                list1End = self.getListEnd(list1, currLength)
                if not list1End: break
                # Make list1 end be None
                list2 = list1End.next
                list1End.next = None
                # Make list2 end be None and store next pair start
                list2End = self.getListEnd(list2, currLength)
                # If list2End exist means we have next subList
                if list2End:
                    nextStart = list2End.next
                    list2End.next = None
                    # Merge list1 and list2 and reconnect tail to next pair
                    currHead, tail = self.mergeList(list1, list2)
                    prevTail.next = currHead
                    prevTail = tail
                    list1 = nextStart
                else:
                    currHead, tail = self.mergeList(list1, list2)
                    prevTail.next = currHead
                    break
            currLength *= 2
            
        return dummyHead.next
        
        
    def countLengthOfList(self, head):
        count = 0
        minimumValue = float('inf')
        currNode = minNode = head
        while currNode:
            currNode = currNode.next
            count += 1
        return count
        
        
    def getListEnd(self, node, curLength):
        curLength -= 1 
        while node and curLength > 0:
            node = node.next
            curLength -= 1
        return node
            
    
    def mergeList(self, node1, node2):
        dummy = ListNode(0)
        tail = dummy
        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        if node1:
            tail.next = node1
        if node2:
            tail.next = node2
        while tail.next:
            tail = tail.next
        return dummy.next, tail
