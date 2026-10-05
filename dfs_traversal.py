graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

stack = ['A']
visited = set()
dfs_order = []

while stack:
    node = stack.pop()

    if node not in visited:
        visited.add(node)
        dfs_order.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

print("DFS Traversal:", " -> ".join(dfs_order))