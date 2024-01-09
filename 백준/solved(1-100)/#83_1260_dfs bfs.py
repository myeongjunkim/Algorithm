import sys
from collections import deque
input=sys.stdin.readline

N, M, V = map(int, input().split())

gragh = [ [] for i in range(N+1)  ]
for i in range(M):
    a, b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

# print(gragh)

visited = [False]*(N+1)
def dfs(gragh, pos, visited):
    visited[pos] = True
    print(pos, end=" ")
    nearby = sorted(gragh[pos])
    for p in nearby:
        if not visited[p]:
            dfs(gragh, p, visited)


dfs(gragh, V, visited)
print("")


visited = [False]*(N+1)
def bfs():
    q = deque()
    q.append(V)
    visited[V] = True
    while q:
        pos = q.popleft()
        print(pos, end=" ")
        nearby = sorted(gragh[pos])
        for p in nearby:
            if not visited[p]:
                visited[p] = True
                q.append(p)

bfs()


