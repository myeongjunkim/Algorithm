import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - R, C 는 1500 (큰편임)
  - X 는 . 이랑 접촉시 댜음날 녹음
구현:
  - 얼음이 녹는 변화를 위한 함수
    - 모든 노드를 순회하면서 인접 . 이 있는 노드 체크
    - 체크된 노드는 전부 . 으로 변환
    - 다음날의 _map 반환
  - L 과 L 이 만날 수 있는지 여부를 체크하는 함수
  - 
"""



def solution(_map):
  R, C = len(_map), len(_map[0])
  visited_W = [[False]*C for _ in range(R)]
  visited_L = [[False]*C for _ in range(R)]

  start_q, water_q = deque(), deque()
  for r in range(R):
    for c in range(C):
      if _map[r][c] == "L":
        start_q.append((r,c))
        _map[r][c] = "."
      if _map[r][c] == ".":
        water_q.append((r,c))
        visited_W[r][c] = True
        
  end = start_q.pop()
  time = 0
  while True:
    water_q = melt_border(_map, water_q, visited_W)
    start_q = bfs(_map, start_q, end, visited_L)
    if not start_q:
      return time
    time += 1


def bfs(_map, start_q, end, visited_L):
  R, C = len(_map), len(_map[0])

  new_start_q = deque()

  while start_q:
    r,c = start_q.popleft()
    if (r,c) == end:
      return deque()
    visited_L[r][c] = True

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
      new_r, new_c = r+dr, c+dc
      if not (0<=new_r<R and 0<=new_c<C):
        continue
      if visited_L[new_r][new_c]:
        continue
      if _map[new_r][new_c] == "X":
        new_start_q.append((new_r, new_c))
      if _map[new_r][new_c] == ".":
        start_q.append((new_r,new_c))
      visited_L[new_r][new_c] = True
  return new_start_q

  


def melt_border(_map, water_q, visited_W):
  new_water_q = deque()
  while water_q:
    r, c = water_q.popleft()
    _map[r][c] = "."
    
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
      new_r, new_c = r+dr, c+dc
      if not (0<=new_r<R and 0<=new_c<C):
        continue
      if visited_W[new_r][new_c]:
        continue
      if _map[new_r][new_c] == "X":
        visited_W[new_r][new_c] = True
        new_water_q.append((new_r, new_c))
        
  return new_water_q



def print_map(_map):
  for line in _map:
    print("".join(line))
  print()

# main
R, C = map(int, input().split())
_map = [ list(input().rstrip()) for _ in range(R) ]
print(solution(_map))


