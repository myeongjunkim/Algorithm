# 2023 KAKAO BLIND RECRUITMENT

from collections import deque
import sys

sys.setrecursionlimit(10**7)

"""
조건:
    - 격자는 가로 세로 50
    - 경로 거리 k 는 2500
    - lrud 사전순으로 가장 빠른 경로 리턴 ( d l r u )
    - 중복 방문 가능
    - impossible 리턴 필요
구현:
    [1차 시도]
    - 문자 순으로 dfs 탐색
    - 이동 거리가 k 일 때 도착지점인지 확인 및 사전식 경로 min 업데이트
    
    [2차 시도]
    - k 와 무관한 최소 경로 탐색
    - 최소 경로를 위한 알파벳 추가
    
    [3차 시도]
    - bfs 를 통한 탐색
"""

min_route = "impossible"


def solution(n, m, x, y, r, c, k):
    global min_route
    pos, goal = (x,y), (r, c)
    # min_route = bfs(n, m, pos, goal, k)
    dfs(n, m, pos, "", goal, k)
    return min_route


def bfs(n, m, start, goal, k):
    total_distance = abs(start[0]-goal[0]) + abs(start[1]-goal[1])
    visited = [[[False]*(m+1) for _ in range(n+1)] for _ in range(k+1)]
    q = deque([(start[0], start[1], "")])
    while q:
        pos_r, pos_c, path = q.popleft()
        visited[len(path)][pos_r][pos_c] = True
        
        if len(path) == k and (pos_r, pos_c) == goal:
            return path
              
        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0] 
        direct = ["d", "l", "r", "u"]
        for i in range(4):
            new_r = pos_r + dr[i]
            new_c = pos_c + dc[i]
            new_path = path+direct[i]
            new_distance = abs(new_r-goal[0]) + abs(new_c-goal[1])
            if len(new_path) > k:
                return "impossible"
            if 1>new_r or n<new_r or 1>new_c or m<new_c:
                continue
            if k-len(path) < new_distance:
                continue
            if visited[len(new_path)][new_r][new_c]:
                continue
            q.append((new_r, new_c, new_path))
            break
            
    return "impossible"       
                
    
def dfs(n, m, pos, path, goal, k):    
    global min_route
    pos_r, pos_c, = pos
    
    if min_route != "impossible":
        return
    if len(path) == k:
        if pos == goal:
            min_route = path
        return
    
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0] 
    direct = ["d", "l", "r", "u"]
    
    for i in range(4):
        new_r = pos_r + dr[i]
        new_c = pos_c + dc[i]
        new_path = path + direct[i]
        new_distance = abs(new_r-goal[0]) + abs(new_c-goal[1])

        if len(new_path) > k:
            return
        if 1>new_r or n<new_r or 1>new_c or m<new_c:
            continue
        if k-len(path) < new_distance:
            continue
        
        dfs(n, m, (new_r, new_c), new_path, goal, k)
        break
        
    
def minimum_route(n, m, x, y, r, c, k):
    
    dr, dc = r-x, c-y
    direct = ["d", "l", "r", "u"]
    
    route = ""
    if dr > 0:
        route += "d"*abs(dr)
    if dc < 0:
        route += "l"*abs(dc)
    if dc > 0:
        route += "r"*abs(dc)
    if dr < 0:
        route += "u"*abs(dr)
    
    print(route)
    
    if len(route) == k:
        return route
    elif len(route) > k:
        return "impossible"
    else:
        
        n = k-route
        if n%2 != 0:
            return "impossible"

#         route = "d" + route + "u"
#         route = "r" + route + "l"
#         route = "l" + route + "r"
        
#         route = route + "rl"
#         route = route + "lr"
            
    
    return route