import sys
from collections import deque
input=sys.stdin.readline


M, N = map(int, input().strip().split())

gragh = []
for i in range(M):
    line = input().strip()
    new_line=[]
    for c in line:
        if c == "-":
            new_line.append(0)
        else:
            new_line.append(1)
    gragh.append(new_line)
    

visited = [[False] * N]*M

# def bfs():
#     q = deque()
#     q.append([0,0])
#     while q:
#         pos = q.popleft()
#         if data[pos[0]][pos[1]] == "-":

cnt = 0

def get_next(pos):
    r, c = pos[0], pos[1]
    nearby = []
    if r != M-1:
        nearby.append([r+1, c])
    if c != N-1:
        nearby.append([r, c+1])
    return nearby

def dfs(gragh, pos, visited):
    r, c = pos[0], pos[1]
    nearby = get_next(pos)
    
    if visited[r][c] is False:
        visited[r][c] = True
        if gragh[r][c] == 0:
            
            