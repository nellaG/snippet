""" dfs.py """


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


def dfs(graph, start):
    start = 1

    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
        print(stack)

    return visited


def dfs_rec(graph, node, visited):
    visited.append(node)

    for i in graph[node]:
        if not (i in visited):
            dfs_rec(graph, i, visited)

    return visited


print(dfs(graph, 1))
print(dfs_rec(graph, 1, []))
