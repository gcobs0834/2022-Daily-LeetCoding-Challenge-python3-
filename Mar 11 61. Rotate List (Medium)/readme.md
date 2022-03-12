**[LeetCode Discuss](https://leetcode.com/problems/rotate-list/discuss/1838844/pythongoc-rotate-solution-and-explanation)**
# [Python/GO/C++] 🌟 Rotate Solution and Explanation 💕
## 1️⃣ Main Idea:
By example```[1,2,3,4,5], k = 2``` The answer will be move length = 2 tail to head ```[4,5,  1,2,3]```.
Since it's a linked-list, we can only traverse whole linked-list from head to tail. So we have to find the length before **k length tail** first.
But in example 2 ```head = [0,1,2], k = 4``` We can k mod 3 = 1, to calculate new k value. And move 2 to be new head ```[2,0,1]```

**Algo**
1. Calculate **length** of linked-list, and make it **circular** (We will break circular at final step)
2. Make k %= length, and calculate **lengthPrev** to be length before k element => lengthPrev = length - k - 1 (1 will be initial length when we start from head)
3. Traverse linked-list from head, once curr in the lengthPrev node, we know it's new tail of result
	newHead = curr.next, and make curr.next = None
4. return newHead
## Complexity Analysis
* Time: O(N): Let N be the length of linked list
* Space: O(1)

## Code

**Python**
```python
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
```
**Go**
```go
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil{
        return head
    }
    
    length := 1
    curr := head
    // Calculate length of linked-list and make it circular
    for curr.Next != nil{
        length += 1
        curr = curr.Next
    }
    curr.Next = head
    // Calculate length before k element
    k %= length
    lengthPrev := length - k - 1
    curr = head
    // Move curr to new tail
    for i := 0; i < lengthPrev; i++{
        curr = curr.Next
    }
    // New head would be tail.next
    res := curr.Next
    // Make tali point to None
    curr.Next = nil
    
    return res
}
```
**C++**
```C++
// O(N) | O(1)
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) return head;
        int length = 1;
        ListNode* curr = head;
        while (curr->next){
            length++;
            curr = curr->next;
        }
        curr->next = head;
        
        k %= length;
        int lengthPrev = length - k - 1;
        curr = head;
        for (int i = 0; i < lengthPrev; i++){
            curr = curr->next;
        }
        ListNode* res = curr->next;
        curr->next = nullptr;
        return res;
    }
};
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
