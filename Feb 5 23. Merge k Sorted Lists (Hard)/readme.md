# [Python 3] ➗ Divide and Conquer Solution➗

## Before Solving This Question
In this question, make sure you know how to merge two sorted linked-list in **[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)**

## Merge One By One 😣
We merge every linked-list pop from lists one by one, eventually we have to do **k-1** times merge.

## Complexity Analysis
* Time: O(kN) : Let *N* be the length of  Linked-List, *k* be numbers of Linked-List in lists
* Space: O(1) 

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/9834903cfb868857c43c3a75d3511f682bed1dbe/Feb%205%2023.%20Merge%20k%20Sorted%20Lists%20(Hard)/Solution.py#L2)

## 👍👍Divide and Conquer (Optimal)👍👍
Instead of merge linked-lists one by one take  **k-1**. We merge linked listed 2 after 2 => So we will **divide length of lists by 2** every time, eventually we will divide it into **log(k)** which takes log(k)
## Complexity Analysis
* Time: O(N log k) :  Let *N* be the length of  Linked-List, *k* be numbers of Linked-List in lists
* Space: O(1)

## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/9834903cfb868857c43c3a75d3511f682bed1dbe/Feb%205%2023.%20Merge%20k%20Sorted%20Lists%20(Hard)/Solution.py#L31)


# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

## Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
## Example 2:

Input: lists = []
Output: []
##Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
