class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        currentNode, i = self.head, 0 # i = Traversed length of linked list
        while currentNode:
            if random.randint(0, i) == 0: # if i =0, means 1/1 selected, if i = 1, means 1/2 updated ans etc.
                ans = currentNode.val
            currentNode = currentNode.next
            i += 1
        return ans
