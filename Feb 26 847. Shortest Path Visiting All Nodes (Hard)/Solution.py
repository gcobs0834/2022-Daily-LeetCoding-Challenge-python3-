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
