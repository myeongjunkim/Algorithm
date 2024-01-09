import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, queue, cnt, visited):
    R, C = len(graph)-2, len(graph[0])-2
    while queue:
        points = queue.popleft()
        new_points = []
        for point in points:
            if not visited[(point[0]-1)*C + point[1]-1]:
                visited[(point[0]-1)*C+ point[1]-1] = True
                if point[0] == R and point[1] == C:
                    return cnt
                nearby_points = get_nearby(graph, point)
                new_points.extend(nearby_points)
        cnt +=1
        queue.append(new_points)

def get_nearby(graph, point):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    nearby_points=[]
    for i in range(4):
        new_r = point[0] + dr[i]
        new_c = point[1] + dc[i]
        if graph[new_r][new_c] == 0:
            continue
        nearby_points.append([new_r,new_c])
    return nearby_points

def solution():
    N, M = map(int, input().split())
    map_list = [ [0]*(M+2) ]
    visited=[False]*(M*N)
    for i in range(N):
        line = input().strip()
        line_list = [0]
        for c in line:
            line_list.append(int(c))
        line_list.append(0)
        map_list.append(line_list)
    map_list.append([0]*(M+2))
    queue=deque()
    queue.append([[1,1]])
    print(bfs(map_list, queue, 1, visited))

solution()