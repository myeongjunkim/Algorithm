import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - N, M 은 1000
  - 최대 이동거리 K 는 1000
  
구현:
 - get_nearby 함수를 통해 인접노드를 구한다.
 - K 만큼 이동할 경우 이동경로에 있는 노드들의 visited 를 관리해준다.
 - bfs 를 통해 최소 시간을 구한다.
 
"""

def solution(N, M, _map, start, end, K):

  visited = [ [0]*M for _ in range(N) ]
  q = deque([start])
  while q:
    r, c = q.popleft()
    if (r, c) == end:
      return visited[r][c]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
      for k in range(1, K+1):
        new_r, new_c = r+dr[i]*k, c+dc[i]*k
        if new_r<0 or new_r>N-1 or new_c<0 or new_c>M-1: 
            break
        if _map[new_r][new_c] == "#" :
            break
        if visited[new_r][new_c] and visited[r][c] >= visited[new_r][new_c]:
          break
        if not visited[new_r][new_c]:
          q.append((new_r, new_c))
          visited[new_r][new_c] = visited[r][c] + 1
        
  return -1

  

# main
N, M, K = map(int, input().split())
_map = [ input().strip() for i in range(N) ]
x1, y1, x2, y2 = map(int, input().split())
start= ( x1 - 1, y1 - 1 )
end  = ( x2 -1, y2 - 1 )
print(solution(N, M, _map, start, end, K))