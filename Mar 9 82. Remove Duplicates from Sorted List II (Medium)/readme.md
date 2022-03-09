**[LeetCode Discuss Post](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1833627/pythongo-dummy-node-solution-and-explanation)**

# [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

## Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
## Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.


# [Python/Go] 🌟 Dummy Node Solution and Explanation 💕

## 1️⃣ Main Idea:
It is very important to set a dummy node **points to head**, in this question the head of linked lists will be change if original head is duplicate

For Example 2

	head = [1,1,1,2,3], Output: [2,3]

You can see that we change head to 2, so it's important to set a dummy node before head and then we return dummy.next

Another requirement for this question is that we have to remove duplicate nodes.

**Algorithm**

0. We set a prev node, before we traverse into list
1. We set subHead = prev.next, and sent it to traverse the list.
Once we find that **subHead.val != subHead.next.val** means subHead is not duplicate, we can move prev.next = subHead, and move prev forwar
2. If we find that subHead is **duplicate**, and then move subHead = subHead.next until **subHead.val != subHead.next.val** (Could be None or new value)
And then we make **prev.next = subHead.next**
Note that we not move prev forward at this stage, only remove duplicate. We only move prev forward to non duplicate nodes which will be excute at step2
## Complexity Analysis
* Time: O(N): Let N be the length of linked list
* Space: O(1)
## Floyd's Cycle Detection Code
**Python**
```python
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
```
**Go**
```go
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
```
