from heapq import heappush, heappop

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, v):
        visited = []
        while self.parent[v] != v:
            visited.append(v)
            v = self.parent[v]
        
        for visited_node in visited:
            self.parent[visited_node] = v
        
        return v

    def union(self, u, v):
        p1, p2 = self.find(u), self.parent(v)
        if p1 == p2:
            return False
        
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        
        return True

def minimum_spanning_tree(edges, n):
    dsu = UnionFind(n)
    min_heap = []
    for u, v, weight in edges:
        heappush(min_heap, [weight, u, v])
    
    mst = []
    while len(mst) < n - 1: # (n - 1) == max number of edges
        _, u, v = heappop(min_heap)
        if dsu.union(u, v):
            mst.append([u, v])
    
    return mst
