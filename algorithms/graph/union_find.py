from collections import defaultdict

# Optimized Using Weight
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.find(self.parent[x]))
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return 
        
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]

    
    def is_connected(self, x, y):
        return self.parent[x] == self.parent[y]
    
union = UnionFind(size=4)

# Optimized Using Rank
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.find(self.parent[x]))
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return 
        
        if self.size[p1] == self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]

    
    def is_connected(self, x, y):
        return self.parent[x] == self.parent[y]
    

# Yeabsira's Implementation
class YeabsiraFind:
    def __init__(self, size):
        self.parent = [-1 for i in range(size + 1)]
    
    def find(self, node):
        if self.parent[node] < 0:
            return node
        
        visited = []
        while self.parent[node] > 0:
            visited.append(node)
            node =  self.parent[node]
        
        for visited_node in visited:
            self.parent[visited_node] = node
        
        return node

    def union(self, set1, set2):
        p1 = self.find(set1)
        p2 = self.find(set2)

        if p1 == p2:
            return 
        total_nodes = self.parent[p1] + self.parent[p2]
        if self.parent[p1] > self.parent[p2]:
            self.parent[p1] = p2
            self.parent[p2] = total_nodes
        else:
            self.parent[p2] = p1
            self.parent[p1] = total_nodes

    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(int)
    
    def find(self, v):
        if v not in self.parent:
            self.parent[v] = v

        visited = []
        while self.parent[v] != v:
            visited.append(v)
            v = self.parent[v]
        
        for visited_node in visited:
            self.parent[visited_node] = v
        
        return v

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False
        
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        
        return True