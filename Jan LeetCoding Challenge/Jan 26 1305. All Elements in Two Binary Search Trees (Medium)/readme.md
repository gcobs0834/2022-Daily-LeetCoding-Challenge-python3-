# Python 3 Solution Time: O(N+M) Space: O(N+M) 
## Recursive Solution
> Step1. We can do **inorder-traversal** for both tree1 and tree2 and that will gives us two sorted array *list1* and *list2*
> Step2. Merge two sorted list and return
## Complexity Analysis
* Time: O(N + M) : *N* and *M* represent length of tree1 an tree2. We traverse tree1 and tree2 take O(N+M) and then merge two list also take O(N+M) => O(2(N+M)) => O(N+M) 
* Space: O(N + M) : *N* and *M* represent length of tree1 an tree2. List1, List2 takes O(N+M) and final output list also takes O(N+M) and recursive call takes O(max(h1,h2)) so we consider O(N+M)

## Python Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Jan%2026%201305.%20All%20Elements%20in%20Two%20Binary%20Search%20Trees%20(Medium)/Solution.py)


# Better Solution
## Iterative  Solution
> Step1. Instead of merge two sorted array after inorder-traversal, we append it in the traversal while each time we find nextNode in the traversal
> Contition: If tree1Node.val <= tree2Node.val => We append tree1Node.val in res and then traverse tree1Node to nextNode
> Step2. Return res
## Complexity Analysis
* Time: O(N + M) : *N* and *M* represent length of tree1 an tree2. This will take same time above
* Space: O(N + M) : *N* and *M* represent length of tree1 an tree2. We can reduce space complexity by only O(h1 + h2) + O(N+M), where *h1*, *h2* is length of stack and then O(N+M) is output list, but it still O(N + M) 

## Python Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/main/Jan%2026%201305.%20All%20Elements%20in%20Two%20Binary%20Search%20Trees%20(Medium)/Solution.py)


# [1305. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
# Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
