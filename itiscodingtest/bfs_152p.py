"""
미로탈출 152p

5 6
101010
111111
000001
111111
111111

-> 10

3 3
110
010
011

->5

"""

import sys
from collections import deque
input = sys.stdin.readline

# global
ROW, COL = map(int, input().split())
graph = []
for _ in range(ROW):
    graph.append(list(map(int, input().strip())))




def bfs():
    visited = [[False]*COL for _ in range(ROW)]
    graph_dir = [[1]*COL for _ in range(ROW)]


    start = [0,0]
    q = deque([start])
    while q:
        x, y = map(int, q.popleft())
        visited[x][y] = True
        if x == ROW-1 and y ==COL-1:
            return graph_dir[x][y]

        for nby in get_nby(x,y):
            nx, ny = map(int, nby)
            if visited[nx][ny] or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph_dir[nx][ny] = graph_dir[x][y] + 1
                q.append([nx,ny])

        """
        x,y 방문 찍기

        x, y의 nby 애들 찾기(좌표만 걸러)
        if nby : cnt +=1
        nby 애들 돌면서
            도착점이면 return cnt
            방문 안하고, 1인 놈 
                q 에 싸그리 넣기
        
        """

def get_nby(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    nbys = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=ROW or ny<0 or ny>=COL:
            continue
        nbys.append([nx, ny])

    return nbys


print(bfs())