from collections import defaultdict, deque
# D.A.G -> Directed Asyclic Graph

def main():
    # n - number of node, m - number of edges
    n, m = map(int, input().split())

    graph = defaultdict(list)
    indegree = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1
    
    order = []
    level = []
    for node, node_indegree in enumerate(indegree):
        if node_indegree == 0:
            level.append(node)
            order.append(node)
    
    level = deque(level)
    while level:
        node = level.popleft()
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                order.append(neighbour)
                level.append(neighbour)
    print(order)

main()