class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        uf = UnionFind(n)
        logs.sort(key = lambda x: x[0])
        groups = n
        for timestamp, f1, f2 in logs:
            groups -= uf.union(f1, f2)
            if groups == 1:
                return timestamp
        return -1
        
class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        
    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1
