graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['B'],
}

start = 'A'
visited = []
queue = [start]
while queue:
    ele = queue.pop(0)
    if ele not in visited:
        visited.append(ele)
        queue.extend(graph[ele])
print(visited)