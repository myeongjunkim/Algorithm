import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

"""
조건:
  - N(4 ≤ N ≤ 50)
  - M(1 ≤ M ≤ 10)
  
구현:
  - 바이러스 위치를 다 구한다.
  - (총개수-M) 개만큼 combinations 하여 해당 위치는 0 으로 바꾼다.
  - r, c 돌면서 visited 도 안되고, _map[r][c] 가 1도 아닌 경우가 있으면 -1 return 한다.
  - 아니라면 d return 한다.
  
"""

def solution(N, M, _map):
  def get_starts():
    starts = []
    for r in range(N):
      for c in range(N):
        if _map[r][c] == 2:
          starts.append((r,c))
    return starts
  def bfs(starts):
    visited = [ [0]*N for _ in range(N) ]
    q = deque(starts)
    while q:
      r, c = q.popleft()

      for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_r, new_c = r+dr, c+dc
        if not (0<=new_r<N and 0<=new_c<N):
          continue
        if visited[new_r][new_c] or (new_r, new_c) in starts:
          continue
        if _map[new_r][new_c] == 1:
          continue
        q.append((new_r, new_c))
        visited[new_r][new_c] = visited[r][c] + 1
        
    time = 0
    for r in range(N):
      for c in range(N):
        if _map[r][c] != 0:
          continue
        if not visited[r][c]:
          return -1
        else:
          time = max(time, visited[r][c])
        
    return time

  min_result = []
  starts = get_starts()
  for new_starts in combinations(starts, M):
  
    result = bfs(new_starts)
    if result >= 0:
      min_result.append(result)
      
  
  return min(min_result) if min_result else -1

  
# main
N, M = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(N)]
print(solution(N,M, _map))
