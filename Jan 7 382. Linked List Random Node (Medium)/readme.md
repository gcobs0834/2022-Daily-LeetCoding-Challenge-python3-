# Python 3 Solution O(N)

* Time O(N) for travere all node in linked-list
* Space O(1) we only store ans, which is constant space

> Simple Follow Up:
input: ['a', 'b', 'c', 'd', 'e']

1. sees  'a' , seen['a'] so a must be 1/1 selected ans = a
2. sees 'b' , seen['a', 'b'] so b would be 1/2 prob update ans = 1/2(ans), 1/2(b)
3. sees 'c' , seen['a', 'b', 'c'] so c would be 1/3 prob update ans = 2/3(ans), 1/3(c)
4. sees 'd', seen['a', 'b', 'c', 'd'] so d would be 1/4 prob update ans = 3/4(ans), 1/4(d)
5. sees 'e', seen['a', 'b', 'c', 'd', 'e'] so d would be 1/5 prob update ans = 4/5(ans), 1/5(e)

* Every iteration we increse the Denominator of probability and make ans update by reservoir



# 382. [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)
Medium

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the integer array nums.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.
 

## Example 1:


Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

Constraints:

The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.
