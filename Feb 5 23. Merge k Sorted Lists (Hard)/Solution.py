# Merge one by one O(kN) | O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        
        LL1 = lists.pop()
        while lists:
            LL2 = lists.pop()
            LL1 = self.merge2List(LL1, LL2)
        return LL1
        
    def merge2List(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
      
# Merge two and two O(N log k) | O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        
        while len(lists) > 1:
            newLists = [] 
            for i in range(0, len(lists), 2):
                LL1 = lists[i]
                LL2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList = self.merge2List(LL1, LL2)
                newLists.append(mergedList)
            lists = newLists
        return lists[0]
                
    def merge2List(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next

            
