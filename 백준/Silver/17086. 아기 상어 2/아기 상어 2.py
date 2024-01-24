import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - 2 ≤ N, M ≤ 50
  - 안전거리 -> 주변 1까지 최단 거리
  - 대각선도 인접노드
  
구현:
 - 전체 노드 돌면서 0인 노드의 최단거리 구해서 최대값으로 최신화
 - bfs 를 통해 최단거리 구하기
 

"""

def solution(N, M, _map):

  max_value = 0
  
  for r in range(N):
    for c in range(M):
      if not _map[r][c]:
        value = bfs((r,c), N, M, _map)
        max_value = max(max_value, value)

  return max_value


def bfs(start, N, M, _map):
  visited = [ [0]*M for _ in range(N) ]

  dr = [ 0, 0, 1, 1, 1, -1, -1, -1 ]
  dc = [ 1, -1, 0, 1, -1, 0, 1, -1 ]

  q = deque([start])
  while q:
    r, c = q.popleft()
    if _map[r][c]:
      return visited[r][c]

    for i in range(8):
      next_r, next_c = r+dr[i], c+dc[i]
      if next_r<0 or next_r>N-1 or next_c<0 or next_c>M-1:
        continue
      if visited[next_r][next_c]:
        continue
      q.append((next_r, next_c))
      visited[next_r][next_c] = visited[r][c] + 1
  
  return -1

# main
N, M = map(int, input().split())
_map = [ list(map(int, input().split())) for i in range(N) ]
print(solution(N, M, _map))