import sys
from collections import deque

input = sys.stdin.readline

"""
조건:
  - 
  
구현:
  - 
"""

def solution(N, M, K, _map):
          
    visited = [ [ [ 0 for _ in range(M)] for _ in range(N)] for _ in range(K+1) ]
    visited[0][0][0] = 1

    q = deque([ (int(0),int(0), int(0), int(1)) ])
    while q:
      wall, r, c, time  = q.popleft()
      if (r,c) == (N-1, M-1):
        return time
      for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_r, new_c = r+dr, c+dc
        if not (0<=new_r<N and 0<=new_c<M):
          continue
        if visited[wall][new_r][new_c]:
          continue
        if _map[new_r][new_c] == "1" :
          if wall < K and not visited[wall+1][new_r][new_c]:
            if time%2 == 1:
              q.append(( wall+1, new_r, new_c, time+1 ))
              visited[wall+1][new_r][new_c] = 1
            else:
              q.append(( wall, r, c, time+1 ))
          continue
        
        q.append(( wall, new_r, new_c, time+1 ))
        visited[wall][new_r][new_c] = 1
        
    return -1

  
  
  
# main
N, M, K = map(int, input().split())
_map = [ list(input().strip()) for _ in range(N) ]
print(solution(N,M, K, _map))

