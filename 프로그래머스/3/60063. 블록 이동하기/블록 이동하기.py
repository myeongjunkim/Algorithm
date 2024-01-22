# 2020 KAKAO BLIND RECRUITMENT

from collections import deque

# 7:45



"""
조건: 
    - 로봇의 회전 조건 검증 필요
    - N 은 100 이하
    - 로봇은 2칸 차지, 회전 해도 같음
구현: 
    - bfs 를 통해 구현
    - 특정 칸을 차지했을 때 로봇이 갈 수 있는 다음 pos 조사
    - 3차원 배열 visited 운영 및 distance 관리
        [dir][r][c] 
            dir:0 -> r,c 기준 우측 가로, 
            dir:1 -> r,c 기준 하측 세로
    - 다음 pos 조사
        - 상단 두개 가능 여부 조사 
            [위로 이동, 왼-상 회전, 오-상 회전]
        - 하단 두개 가능 여부 조사
            [아래로 이동, 왼-하 회전, 오-하 회전]
        - 좌 우 조사
            [왼 이동, 오 이동]
        
"""

def solution(board):
    N = len(board)
    visited = [[ [0 for _ in range(N)] for _ in range(N) ] for _ in range(2) ]
    pre_node = [[ [(0,0,0) for _ in range(N)] for _ in range(N) ] for _ in range(2) ]

    q = deque([(0,0,0)])
    while q:
        dir, r, c = q.popleft()
        
        if dir == 0 and r == N-1 and c+1 == N-1:
            # print("result")
            # pre_dir, pre_r, pre_c = dir, r, c
            # for i in range(visited[dir][r][c] + 1):
            #     print(pre_dir, pre_r, pre_c)
            #     pre_dir, pre_r, pre_c = pre_node[pre_dir][pre_r][pre_c]
            return visited[dir][r][c]
        
        if dir == 1 and r+1 == N-1 and c == N-1:
            return visited[dir][r][c]

        for nearby in get_nearby(dir, r, c, board):
            new_dir, new_r, new_c = nearby
            if visited[new_dir][new_r][new_c]:
                continue
            visited[new_dir][new_r][new_c] = visited[dir][r][c] + 1
            pre_node[new_dir][new_r][new_c] = (dir, r, c)
            q.append((new_dir,new_r,new_c))
    
    return 0

def get_nearby(dir, r, c, board):
    
    N = len(board)
    nearby = []
    
    if dir == 0:
        # 상
        if r > 0 and not board[r-1][c] and not board[r-1][c+1]:
            nearby.append((1, r-1, c))
            nearby.append((1, r-1, c+1))
            nearby.append((0, r-1, c))
        # 하
        if r < N-1 and not board[r+1][c] and not board[r+1][c+1]:
            nearby.append((1, r, c))
            nearby.append((1, r, c+1))
            nearby.append((0, r+1, c))
            
        # 좌
        if c > 0 and not board[r][c-1]:
            nearby.append((0, r, c-1)) 
        # 우
        if c < N-2 and not board[r][c+2]:
            nearby.append((0, r, c+1)) 
            
    else:
        # 좌 
        if c > 0 and not board[r][c-1] and not board[r+1][c-1]:
            nearby.append((0, r, c-1))
            nearby.append((0, r+1, c-1))
            nearby.append((1, r, c-1))
        # 우 
        if c < N-1 and not board[r][c+1] and not board[r+1][c+1]:
            nearby.append((0, r, c))
            nearby.append((0, r+1, c)) 
            nearby.append((1, r, c+1))
        
        # 상
        if r > 0 and not board[r-1][c]:
            nearby.append((1, r-1, c))
        # 하
        if r < N-2 and not board[r+2][c]:
            nearby.append((1, r+1, c))
        
    return nearby

    
    