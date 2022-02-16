
# 🌟[Python 3] Pair Nodes Solutions and Explanation


## 1️⃣ Approach 1:

* In every swap linked list question, you should always think about **temp holder** which point to next node.
* And once init these temp holder, we can **swap** on these nodes  which follows description.
* After swapping, we **update** current pointers to temp holder
* In this question we separate nodes into pairs since we have to swap between these pair


> Step 1. **Init temp holder** Use nextPair to store next pair's position
> Step 2. **Swap**, make second point to first, prev point to second, and first point to nextPair
> Step 3. **Update**: Update prev and current pointer to corresponding temp holder

## Complexity Analysis
* Time: O(N) : Let n be length of nodes
* Space: O(1) 

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Feb%2016%2024.%20Swap%20Nodes%20in%20Pairs%20(Medium)/Solution.py)

# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

## Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
## Example 2:

Input: head = []
Output: []
## Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
