import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

"""
조건:
  - 3 ≤ N, M ≤ 8
  - 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
  - 바이러스가 퍼질 수 없는 곳을 안전 영역
구현:
  - 맵의 칸을 전부 조사한다.
  - 0칸은 저장한다. 1칸은 visited True 로 바꾼다.
  - 0 칸에서 3개를 뽑아 visited True 로 바꾼다.
  - 2 칸을 모두 q 에 넣고 bfs 진행한다.
  - visited False 이면서 0 인 개수를 조사하여 최대값 업데이트 한다.
  
  
  
"""

def solution(N, M, _map):
  def get_map_info(_map):
    starts, zero = [], []
    for r in range(N):
      for c in range(M):
        if _map[r][c] == 0:
          zero.append((r,c))
        elif _map[r][c] == 2:
          starts.append((r,c))
    return starts, zero
 
  def bfs(starts, _map):
    visited = [[False]*M for _ in range(N)]
    for r,c in starts:
      visited[r][c] = True
    
    q = deque(starts)
    while q:
      r, c = q.popleft()

      for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_r, new_c = r+dr, c+dc
        if not (0<=new_r<N and 0<=new_c<M):
          continue
        if visited[new_r][new_c]:
          continue
        if _map[new_r][new_c] != 0:
          continue
        q.append((new_r, new_c))
        visited[new_r][new_c] = True

    result = 0
    for r in range(N):
      for c in range(M):
        if not visited[r][c] and _map[r][c] == 0:
          result += 1
  
    return result


  max_result = 0
  starts, zero = get_map_info(_map)
  for z1,z2,z3 in combinations(zero, 3):
    _map[z1[0]][z1[1]], _map[z2[0]][z2[1]], _map[z3[0]][z3[1]] = 1, 1, 1
    max_result = max(max_result, bfs(starts, _map))
    _map[z1[0]][z1[1]], _map[z2[0]][z2[1]], _map[z3[0]][z3[1]] = 0, 0, 0

  return max_result

# main

N, M = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(N) ]
print(solution(N,M,_map))
