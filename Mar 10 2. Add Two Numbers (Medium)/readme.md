**[Leetcode Discuss Post](https://leetcode.com/problems/add-two-numbers/discuss/1836297/pythongo-2-different-solutions-and-explanations)**
# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

## Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
## Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
## Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

# [Python/Go] 🌟 2 Different Solutions and Explanations 💕

## 1️⃣Calculate Actual Sum Approach (Python Only Not Recommended):
**This will only work at python3 because python support very big integer and don't have to worry about BigInt or int type**

1. Iterate through l1 and l2 to calculate whole l1 and l2's value represent by l1Num and l2Num.
2. Sum up l1Num and l2Num and use remainder of totalSum to create a output linked-list

## Complexity Analysis
* Time: O(max(m, n)): Let m and n represent length of l1 and l2
* Space: O(max(m, n)): Let m and n represent length of l1 and l2
## Code
**Python**
```python
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
```

## 2️⃣ Create a New linked-list and Carry In Approach:
Instead of sperate sum up l1 and l2, we can acutally create a new node while we traverse through l1 and l2. And be careful for the carry in.

**Algo**

* Iterate through l1 and l2,
	1. Every iteration we add up l1.val, l2.val **and carry**. 
	2. Create a new node and make curr points new node.
	3. Move l1, l2, curr forward. And pass **carry** to next iteration
* If carry != 0, create a new node and make curr points to new node

## Complexity Analysis
* Time: O(max(m, n)): Let m and n represent length of l1 and l2, at total will be O(max(m,n) + 1) => O(max(m, n)) (**If carry not empty**)
* Space: O(max(m, n)): Let m and n represent length of l1 and l2
## Code
**Python**
```python
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
```
**Go**
```go
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := ListNode{0, nil}
    curr := &dummy
    carry := 0
    for l1 != nil || l2 != nil{
        // Calculate value and carry
        val1, val2 := 0, 0
        if l1 != nil{
            val1 = l1.Val
        }
        if l2 != nil{
            val2 = l2.Val
        }
        currValue := (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) / 10
        // Create a new node, and make curr.next point to it
        curr.Next = &ListNode{currValue, nil}
        // # Move curr, l1 and l2 forward
        curr = curr.Next
        if l1 != nil{
            l1 = l1.Next
        }
        if l2 != nil{
            l2 = l2.Next
        }  
    }
    // if carry != 0 means we have to create a new node
    if carry != 0{
        curr.Next = &ListNode{carry, nil}
    }
    
    return dummy.Next
}
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
