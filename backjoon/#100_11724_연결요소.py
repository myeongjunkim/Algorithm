import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def save_grap(N, M):
    grap = [
        [] for _ in range(N +1)
    ]

    for i in range(M):
        v1, v2 = map(int, input().split())
        grap[v1].append(v2)
        grap[v2].append(v1)

    return grap

def dfs(grap, v, visited):
    visited[v] = True
    for node in grap[v]:
        if not visited[node]:
            dfs(grap, node, visited)

def execute_dfs():
    N, M = map(int, input().split())
    grap = save_grap(N, M)
    visited = [False]*(N+1)
    cnt = 0
    for v in range(1,N+1):
        if not visited[v]:
            cnt += 1
            dfs(grap, v, visited)
    print(cnt)

    


def execute_bfs():
    N, M = map(int, input().split())
    grap = save_grap(N, M)
    visited = [False]*(N+1)
    cnt = 0


    for start in range(1, N+1):
        if not visited[start]:
            cnt +=1
            q = deque()
            q.append(start)
            visited[start] =True
            while q:
                node = q.popleft()
                for nearby in grap[node]:
                    if not visited[nearby]:
                        visited[nearby] = True
                        q.append(nearby)
            
    print(cnt)


# execute_dfs()
execute_bfs()




