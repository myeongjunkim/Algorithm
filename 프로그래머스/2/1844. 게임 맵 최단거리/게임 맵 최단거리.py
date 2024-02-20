from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [ [False]*M for _ in range(N) ]
    visited[0][0] = True
    
    q = deque([(0,0,1)])
    while q:
        pos_r,pos_c, pos_d = q.popleft()
        for dr, dc in[ (1,0), (-1,0), (0,1), (0,-1)]:
            new_r, new_c, new_d = pos_r+dr, pos_c+dc, pos_d+1
            if (new_r, new_c) == (N-1,M-1):
                return new_d
            if not (0<=new_r<N and 0<=new_c<M ):
                continue
            if not maps[new_r][new_c]:
                continue
            if visited[new_r][new_c]:
                continue
            q.append((new_r, new_c, new_d))
            visited[new_r][new_c] = True
    
    
    return -1