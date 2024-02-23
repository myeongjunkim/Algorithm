import sys

from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
조건:
  - N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
  
구현:
  - 
"""




def solution(N, M, _map):

  def bfs(_map, r,c, id):
    _map[r][c] = id
    q = deque([(r,c)])
    count = 0
    while q:
      r, c = q.popleft()
      count += 1
      for dr, dc in [ (1,0), (-1,0), (0,1), (0,-1) ]:
        new_r, new_c = r+dr, c+dc
        if not (0<=new_r<N and 0<=new_c<M):
          continue
        if _map[new_r][new_c]:
          continue
        q.append((new_r, new_c))
        _map[new_r][new_c] = id
    return count
  
  id_count_map = {}
  id = 1
  for r in range(N):
    for c in range(M):
      if _map[r][c] == 0:
        id += 1
        count = bfs(_map, r,c, id)
        id_count_map[id] = count


  count_map = [ [0]*M for _ in range(N) ]
  for r in range(N):
    for c in range(M):
      if _map[r][c] == 1:
        ids = set()
        
        for dr, dc in [ (1,0), (-1,0), (0,1), (0,-1) ]:
          new_r, new_c = r+dr, c+dc
          if not (0<=new_r<N and 0<=new_c<M):
            continue
          if _map[new_r][new_c] == 1:
            continue
          ids.add(_map[new_r][new_c])
        
        count_map[r][c] = (sum(id_count_map[id] for id in ids)+1) %10

  return count_map
        
  
# main
N, M = map(int, input().split())
_map = [ list(map(int, list(input().strip()))) for _ in range(N) ]
count_map = solution(N,M, _map)
for line in count_map:
  print("".join(map(str, line)))