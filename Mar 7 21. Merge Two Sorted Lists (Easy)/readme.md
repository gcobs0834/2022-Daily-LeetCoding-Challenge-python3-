# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

## Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
## Example 2:

Input: list1 = [], list2 = []
Output: []
## Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


# [Python/Go] 🌟 Iterative Solution and Explanation 💕

## 1️⃣ Iterative Approach:
Step 1. Init a dummy node to keep track of head, once we merged two list we can return **dummy.next**
Step 2. Iterate through list1 and list2, and use a extra pointer **curr** to track current Node
* If list1.val < list2.val: Set curr.next = list1, and move list1's pointer forward
* Else if list1.val > list2.val: Set curr.next = list2, and move list2's pointer forward
* Move curr to curr.next

Step 3. Once we iterate through one of these two list, we make curr.next points to reaming list.

## Complexity Analysis
* Time: O(N+M): Let N and M be length of list1 and list2.
* Space: O(1)
## Iterative Code
**Python**
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to keep track of head
        dummy = ListNode(0)
        curr = dummy
        # Iterate through list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # For remaining
        curr.next = list1 or list2
        
        return dummy.next
```
**Go**
```go
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // Create a dummy node to keep track of head
    dummy := ListNode{}
    curr := &dummy
    // Iterate through list1 and list2
    for list1 !=nil && list2 != nil{
        if list1.Val < list2.Val{
            curr.Next = list1
            list1 = list1.Next
        } else{
            curr.Next = list2
            list2 = list2.Next
        }
        curr = curr.Next
    }
    // For remaining
    if list1 != nil {
        curr.Next = list1
    }
    if list2 != nil {
        curr.Next = list2
    }
    
    return dummy.Next
}
}
```
