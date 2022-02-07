# Python 3 Solution Time: O(N) Space: O(1) 
## Main Idea
In this question we set two pointer:
> first: move to next pointer each time
> second: move to next.next pointer each time

> Step 1: Traverse first and second pointer all the way until they meet
> ( If there is no cycle in the linked list the second pointer will point to None eventually)
> Step 2: Set first back to head and move **BOTH** first and second one step each time. Once they meet then we found the tail.

## Math Explained
Let the whole linked-list's length be *n*, distance between **head** and the **first index** of the cycle be *m*,
The distance between **first index** of the cycle and the **index where first and second pointer meets** to be *p*

We can know that in the step 1: first pointer traverse the distance m+p and the second traverse 2(m + p) and also equals to  n+p => n = 2m + p
Upon this equation if we move second pointer m step it will traverse the linked-list again point at 2m + p which is our target
So in step 2 we move first and second simultaneously in order to find our answer

### IF YOU CAN: Better draw a graph and mark these distance so you will know the whole math equation


## Complexity Analysis
* Time: O(N) : N equals lenghth of linked-list
* Space: O(1)

# [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
