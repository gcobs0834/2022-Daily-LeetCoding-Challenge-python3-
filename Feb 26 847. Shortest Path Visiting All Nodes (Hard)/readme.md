# [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)




# 🌟[Python 3] DFS and BFS Solutions and Explanation 💕

## 1️⃣ DFS Top-Down DP Approach:
* By description **Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.**
We can assume that this would be a DP question, since we want to find minimum length and can visit every node multiple times.

* Since n nodes labeled from 0 to n - 1, we can use a mask to represent if we visited this node before. For example, node = 3, we can use 1000 to represent we visited node3, 1101 => visited 0, 2, 3 nodes

* Another state of our dp solution would be currentNode we at, So the Top-Down DFS would be dfs(node, mask) to return shortest path from **current state**

## DFS Call
We use **backtracking** from dfs(node, endingMask), where endingMask = 111111.. represent every node is visited. So we can generate answer by set **every node** as potential ending point  and use min function to get shortest path

**Base Cases** : 
1. If we visited this state return cache[state]
2. If mask & (mask - 1) == 0 means current mask would only visited 1 node, so return 0.
For example mask = 01000, (mask - 1) = 00111.

**Search Neighbors**
* Iterate through current node's neighbors, and each time we have two branch. **Visited currentNode** and **Not Visited currentNode**. So we make recursive call on both visited and notVisited situaltion.
If visited we don't change mask => visited = 1 + dfs(neighbor, mask), otherwise notVisted = dfs(neighbor, mask ^ (1 << node)) indicates that we haven't visit currentNode so backtrack it by use XOR operation on current mask.
The current state would be **dfs(currentNode, mask) = 1 + min(dfs(neighbor, mask), dfs(neighbor, mask ^ (1 << node)))**

* We have to set cache[state] = float('inf') first, before we make recursive call. Because when we recursive call on visited, its neighbor will points to currentNode it will cause infinity loops.
## Complexity Analysis
* Time: O(N^2 * 2^N) :  The total number of the state would be N * 2^N. And we set every point as ending point to DFS it = > O(N^2 * 2^N)
* Space: O(N * 2^N) : The total number of the state would be N * 2^N. 

## Code
```
# DFS Top-Down DP Solution O(N^2 * 2^N) | O(N * 2^N)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        cache = {}
        def dfs(node, mask):
            state = (node, mask)
            # Base Case
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                return 0
            # Init cache[state] to infinity to avoid endless loop between two nodes
            cache[state] = float('inf')
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    # If already visited currentNode mask doesn't change
                    visited = 1 + dfs(neighbor, mask)
                    # If not visited currentNode set mask = mask ^ (1 << node)
                    notVisited = 1 + dfs(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], visited, notVisited)
            return cache[state]
        
        endingMask = (1 << len(graph)) - 1
        cache = {}
        
        return min(dfs(node, endingMask) for node in range(len(graph)))
```

## 2️⃣ Modified BFS Approach (Optimal)🦐🦐🦐:
When it comes to shortest path, you can immediately think about BFS beacuse while we use BFS each time we can increase level. Once we found target node we can return current level 
* As mentioned before, we are not only consider node itself been visited but also current mask as a state of visited hash map. So we use set visited state = (node, mask)

1. Setup parameters
	* endingMask = (1 << n) - 1
	* We see every node as potential node as first node and its mask would be 1 << node represent we visited this node. 
So we make queue = [(node, 1 << node) for node in range(n)]
	* visited = set(queue) => every visited state would be (node, mask)
	* level = 0
2. BFS Queue
	* Init nextQueue to []
	* Loop through current state in queue and get all their neighbor. And put them into nextQueue if we not visit the neighbor's state
	* Once we found a neighbor's mask == endingMask means at current level we find a path visited all nodes. So return level + 1


## Complexity Analysis
* Time: O(N^2 * 2^N) : The time complexity will equals to DFS but since we don't have to iterate through all possibility, this solution will break early once we found shortest path.
* Space: O(N * 2^N) : The visited stores all states O(N * 2^N)

## Code
```
# BFS O(N^2 * 2^N) | O(N * 2^N)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n = len(graph)
        # If 5 nodes ending mask = 11111
        endingMask = (1 << n) - 1
        # Queue = [(node1, mask1), (node2, mask2) ...]
        queue = [(node, 1 << node) for node in range(n)]
        # Set visited not only by nodes but also currentMask, so the visited states = (node, mask)
        visited = set(queue)
        step = 0
        while queue:
            nextQueue = []
            for node, mask in queue:
                for neighbor in graph[node]:
                    nextMask = mask | (1 << neighbor)
                    # End points means we find shortest path
                    if nextMask == endingMask:
                        return step + 1
                    # Append new state to nextQueue, ignores visited
                    if (neighbor, nextMask) not in visited:
                        visited.add((neighbor, nextMask))
                        nextQueue.append((neighbor, nextMask))
            step += 1
            queue = nextQueue
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
