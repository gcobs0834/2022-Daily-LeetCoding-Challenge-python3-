
# 🌟[Python 3]😎 MergeSort O(logN) and O(1) Space Solutions and Explanation 💕
NOTE: ***Before you solving this question, make sure you know how to merge two sorted linked-list***

## 1️⃣ MergeSort Top-Down O(logN) Space Approach:
> Base Case: If current list is None or contains 1 node, simply return that node
> In recursive call, every time we split list into two part, and make left part of list's end **point to None**, and merge left and right

## Complexity Analysis
* Time: O(N log N) : Merge Sort
* Space: O(log N ) : In recursive call, every time we split list into 2 part => O(log N)

## Top-Down Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/211bef741bfec1f5b22f7d24a51d60a53cf938b0/Feb%2024%20148.%20Sort%20List%20(Medium)/Solution.py#L2)

## 2️⃣ MergeSort Bottom-Up O(1) Space Approach:
* In bottom-up solution. Every time we merge from 1, 2, 4, 8, ... , n node. So we use a while loop and after merge all nodes in currLength, currLength times 2.
> **Step 1**. We count length of the list by function countLengthOfList
> **Step 2**: Iterate through list, and split list into sublists by currLength, once merged all sublist we **increase currLength by times 2** until it's greater or equal length of whole list
> We use getListEnd function to get current sublist's last node, and **break its connection** to next sublist in order to apply mergeList function
> Once we merge two sublist, we make **prevTail points to current sublist's head**.

## Complexity Analysis
* Time: O(N log N) : Merge Sort
* Space: O(1) : We don't use extra space, by bottom up the merge sort solution

## Bottom-Up Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/211bef741bfec1f5b22f7d24a51d60a53cf938b0/Feb%2024%20148.%20Sort%20List%20(Medium)/Solution.py#L44)

# [148. Sort List](https://leetcode.com/problems/sort-list/)

Given the head of a linked list, return the list after sorting it in ascending order.

 

## Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
## Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
## Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
