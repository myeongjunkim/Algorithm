import sys
from collections import deque

input = sys.stdin.readline

# 2:46 ~

"""
조건: 
  - N, M 은 50
  - 문과 열솨 조합으로 길 가능
  - 재방문 가능

구현:
  - BFS 를 통해 구현
  - 열쇠는 리스트를 통해 복사하여 사용 (N, M 이 적으니 가능할듯)
  - 열쇠 복사시 visited 관련한 문제 발생
  - 비트마스킹 방식으로 열쇠의 방문을 처리

"""


KEY = {"a":1, "b":2, "c":4, "d":8, "e":16, "f":32}
DOOR = {"A":1, "B":2, "C":4, "D":8, "E":16, "F":32}

def solution(N, M, _map):
  global KEY, DOOR
  
  start_r, start_c = get_start(N, M, _map)
  start_k = int(0)
  visited = [ [ [0]*M for _ in range(N) ] for _ in range(64) ]
  visited[start_k][start_r][start_c] = 1
  q = deque([(start_k, start_r, start_c)])
  while q:
    k, r, c = q.popleft()
    for dr, dc in [ (1,0), (-1,0), (0,1), (0,-1) ]:
      new_r, new_c = r+dr, c+dc
      if not (0<=new_r<N and 0<=new_c<M):
        continue
      if visited[k][new_r][new_c]:
        continue
      
      if _map[new_r][new_c] == "#":
        continue
      elif _map[new_r][new_c] == "." or _map[new_r][new_c] == "0":
        visited[k][new_r][new_c] = visited[k][r][c] + 1
        q.append((k, new_r, new_c))
      elif _map[new_r][new_c] in KEY:
        new_k = k
        if not (KEY[_map[new_r][new_c]] & k):
          new_k = k + KEY[_map[new_r][new_c]]
        visited[k][new_r][new_c] = visited[k][r][c] + 1
        visited[new_k][new_r][new_c] = visited[k][r][c] + 1
        q.append((new_k, new_r, new_c))
      elif _map[new_r][new_c] in DOOR and DOOR[_map[new_r][new_c]] & k:
        visited[k][new_r][new_c] = visited[k][r][c] + 1
        q.append((k, new_r, new_c))
      elif _map[new_r][new_c] == "1":
        return visited[k][r][c]
        
  return -1


def get_start(N, M, _map):
  for r in range(N):
    for c in range(M):
      if _map[r][c] == "0":
        return (r,c)
  return (0, 0)


# main
N, M = map(int, input().split())
_map = [ list(input().strip()) for _ in range(N) ]
print(solution(N, M, _map))

