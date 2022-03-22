import sys
input=sys.stdin.readline

N = int(input())
M = int(input())


gragh = [ [] for i in range(N+1)  ]
for i in range(M):
    a, b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

# print(gragh)

visited = [False]*(N+1)
cnt = -1
def dfs(gragh, v, visited):
    # print(v, end=" ")
    global cnt
    cnt +=1
    visited[v] = True
    for p in gragh[v]:
        if not visited[p]:
            dfs(gragh, p, visited)


dfs(gragh, 1, visited)
print(cnt)

