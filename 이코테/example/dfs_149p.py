"""
음료수 얼려먹기 149p

4 5
00110
00011
11111
00000
-> 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

dfs 구현
좌표 다 돌면서
    0인 부분 dfs 로 탐색
    cnt += 1

"""

import sys
input = sys.stdin.readline

ROW, COL = map(int, input().split())
graph = []
for _ in range(ROW):
    line = []
    line_str = input()[:-1]
    for c in line_str:
        line.append(int(c))
    graph.append(line)


def dfs(graph, start, visited):
    x, y = start[0], start[1]
    visited[x][y] = True
    # print(start, get_nearby(start))
    for nby in get_nearby(start):
        n_x, n_y = nby[0], nby[1]
        if graph[n_x][n_y] == 1 or visited[n_x][n_y]:
            continue
        dfs(graph, nby, visited)


def get_nearby(pos):
    # pos -> [x, y]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    x,y = pos[0], pos[1]

    nearby = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=ROW or ny<0 or ny>=COL:
            continue
        else:
            nearby.append([nx, ny])

    return nearby

def execute():
    visited = [[False]* COL for _ in range(ROW)]
    cnt = 0
    for x in range(ROW):
        for y in range(COL):
            if not visited[x][y] and graph[x][y] == 0:
                cnt += 1
                dfs(graph, [x,y], visited)

    print(cnt)

execute()