
# 🌟[Python 3]😎 DFS and BFS Solutions and Explanation 💕

## 1️⃣ DFS Approach:
* The tricky part of this question is how do we create a clone node and connect to its clone nodes as well.
 In order to solve this quesition, we use a **hashMap** which store **key = original node** and **value = clone node**
 That is **graphMap[node] = it's clone node**

* In the DFS function, we also use the hashMap as a visited map. Once we see a node in hashMap, we knew that we have already clone this node so we return **graphMap[node]**
 And **for neighbors**, we recurrsive call dfs to create a clone neighbor and append it in cloneNode's neighbors.

## Complexity Analysis
* Time: O(V + E) : Let V be nodes in graph and E be edges in graph
* Space: O(V): The hashmap stores V nodes and althrough we use recursive call on dfs, at maximum it grows at most O(V) stack => O(V)

## DFS Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/e170db5d08611263bba2286c06c2481dccf4a2c9/Feb%2023%20133.%20Clone%20Graph%20(Medium)/Solution.py#L2)

## 2️⃣ BFS Approach:
* We use same hashMap technique as previous to store graph. >> We use a **hashMap** which store **key = original node** and **value = clone node**
 That is **graphMap[node] = it's clone node**
> In BFS queue
> If we not visited the neighbor => we not visited it yet. 1. Append in queue  2.Create its clone 3. Map clone node and original node
> Once we done that we append **graphMap[neighbor]** to **graphMap[currNode]**'s neighbors

## Complexity Analysis
* Time: O(V + E) : Let V be nodes in graph and E be edges in graph
* Space: O(V): The hashmap stores V nodes.


## BFS Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/e170db5d08611263bba2286c06c2481dccf4a2c9/Feb%2023%20133.%20Clone%20Graph%20(Medium)/Solution.py#L24)

# [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

## Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
## Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
## Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
