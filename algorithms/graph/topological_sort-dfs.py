from collections import *

def main():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    order = []
    visited = [0] * n
    def dfs(node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        visited[node] = 1
        for neighbour in graph[node]:
            if dfs(neighbour):
                return True
        visited[node] = 2
        order.append(node)
        return False
    
    for node in range(n):
        if visited[node] == 0:
            if dfs(node):
                return "Cycle Detected"

    return order[::-1]

print(main())