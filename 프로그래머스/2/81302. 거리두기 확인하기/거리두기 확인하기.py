# 2021 카카오 채용연계형 인턴십

from collections import deque

# 16:52 ~ 

"""
조건: 
    - 5x5
    - 응시자 p, 빈테이블 o, 파티션 x
구현:
    - 응시자 좌표 순회
    - visited 가 2일때까지 확인 및 종료
"""

def solution(places):
    result = []
    for place in places:
        flag = True
        for r in range(5):
            if not flag:
                break
            for c in range(5):
                if not flag:
                    break
                if place[r][c] != "P":
                    continue
                if not bfs((r,c), place):
                    flag = False
        result.append(int(flag))            
    return result
        

    
def bfs(start, place):
    
    visited = [ [0]*5 for _ in range(5) ]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    q = deque([start])
    while q:
        r, c = q.popleft()
        if visited[r][c] > 2:
            return True
        elif 0<visited[r][c]<=2 and place[r][c] == "P":
            return False
        for i in range(4):
            new_r, new_c = r+dr[i], c+dc[i]
            if new_r<0 or 4<new_r or new_c<0 or 4<new_c:
                continue
            if place[new_r][new_c] == "X":
                continue
            if visited[new_r][new_c] or (new_r, new_c) == start :
                continue
            q.append((new_r, new_c))
            visited[new_r][new_c] = visited[r][c] + 1
            
    return True