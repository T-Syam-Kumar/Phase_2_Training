graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['B'],
    'E': ['B'],
    'F': ['E'],
    'G': ['B'],
    'H': ['B'],
    'I': ['C'],
}

start = 'A'
visited = []
stack = [start]
while stack:
    ele = stack.pop()
    if ele not in visited:
        visited.append(ele)
        stack.extend(graph[ele])
print(visited)