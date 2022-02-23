# DFS O(V + E)| O(V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge Case
        if node is None:
            return None 
        graphMap = {}
        
        def dfs(node):
            # Means visited
            if node in graphMap: 
                return graphMap[node]
            cloneNode = Node(node.val)
            graphMap[node] = cloneNode
            # Find neighbor
            for neighbor in node.neighbors:
                # DFS neighbors, once create a clone node, append it in neighbors
                cloneNode.neighbors.append(dfs(neighbor))
            return cloneNode
        
        return dfs(node)

# BFS O(V + E)| O(V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge Case
        if node is None:
            return None  
        graphMap = {}
        
        def bfs(node):
            # Init queue
            queue = deque([node])
            graphMap[node] = Node(node.val)
            #Start BFS
            while queue:
                currNode = queue.popleft()
                for neighbor in currNode.neighbors:
                    if neighbor not in graphMap:
                        graphMap[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    # Once we create a clone node, connect to its clone neighbors
                    graphMap[currNode].neighbors.append(graphMap[neighbor])
            return graphMap[node]
            
        return bfs(node)
