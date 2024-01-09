# https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8
import sys
input = sys.stdin.readline


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

max_res = 0
visited = [[False] * N for _ in range(M)]
def execute():
    global max_res
    for i in range(M):
        for j in range(N):
            dfs((i,j), 0, 0)

            nearby_node =[graph[r][c] for r,c in nearby(i,j)]
            if len(nearby_node) == 3:
                max_res = max(max_res, graph[i][j]+sum(nearby_node))
            elif len(nearby_node) == 4:
                max_res = max(max_res, graph[i][j]+sum(sorted(nearby_node)[1:]))
           
            visited[i][j] = False

    print(max_res)


def dfs(v, cnt, total):
    global max_res
    i, j = v
    visited[i][j] = True
    total += graph[i][j]
    if cnt == 3:
        max_res = max(max_res, total)
        return
    for r, c in nearby(i, j):
        if not visited[r][c] :
            dfs((r,c), cnt+1, total)
            visited[r][c] = False


def nearby(r,c):
    res = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = r+dx[i]
        ny = c+dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        res.append((nx, ny))

    return res

execute()