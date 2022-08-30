""" bfs.py """


from collections import deque


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


def bfs(graph, start):
    visited = [start]

    que = deque([start])

    while que:
        node = que.popleft()
        for i in graph[node]:
            if i not in visited:
                que.append(i)
                visited.append(i)
    return visited


print(bfs(graph, 1))
