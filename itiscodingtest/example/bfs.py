# bfs
from collections import deque

graph = [ # n 번 노드의 인접 노드 그래프
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
def bfs(gragh, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        print(node)
        for nearby in gragh[node]:
            if not visited[nearby]:
                q.append(nearby)
                visited[nearby] = True

bfs(graph, 1, visited)