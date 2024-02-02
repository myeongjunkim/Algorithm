import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - R, C 는 100
  - 던지는 횟수 N, 던질때는 좌우 번갈아 가며 던짐
  - 던지는 높이 H, 1~R
  - 클러스터는 한번에 하나씩 떨어진다. 모양이 변하지 않는다.
구현:
  - 높이 H 와 방향 direct 에서 가장 가까운 미네랄을 터트리는 함수 구현
    - map 을 리턴한다.
  - bfs 를 통해 공중에 떠있는 클러스터 찾는 함수 구현
    - 바닥에 붙어있는 독립체는 예외 처리 필요 -> 바닥 인접 판단할 때 조건 고려
  - 클러스터 위치 업데이트 하는 함수 구현
    - 각 열별로 min 좌표 체크
    - 열을 내리면서 처음으로 땅 or x 에 마주칠때 스탑
    - 업데이트 된 map 리턴
"""



def solution(_map, h_list):
  h_list = [len(_map)-h for h in h_list]
  direct = True
  for h in h_list:
    _map = bumb_x(_map, h, direct)
    direct = not direct
    cluster = get_cluster(_map)
    
    if cluster:
      
      down_count = get_down_count(_map, cluster)
      _map = down_cluster(_map, cluster, down_count)
  return _map


def bumb_x(_map, h, direct):
  c_range = range(len(_map[h])) if direct else range(len(_map[h])-1, -1, -1)
  for c in c_range:
    if _map[h][c] == "x":
      _map[h][c] = "."
      break
  return _map


def get_cluster(_map):
  visited = [ [False]*C for _ in range(R) ]
  for r in range(R):
    for c in range(C):
      if _map[r][c] == "." or visited[r][c]:
        continue
      cluster = bfs(_map, (r, c), visited)
      if cluster and max(cluster)[0] != R-1:
        return cluster
  return []


def bfs(_map, start, visited):
  R, C = len(_map), len(_map[0])

  q = deque([start])
  cluster = []
  while q:
    r, c = q.popleft()
    if visited[r][c]:
      continue
    visited[r][c] = True
    cluster.append((r,c))
    for dr, dc in [ (1,0), (-1,0), (0,1), (0,-1) ]:
      new_r, new_c = r+dr, c+dc
      if not (0<=new_r<R and 0<=new_c<C):
        continue
      if visited[new_r][new_c]:
        continue
      if _map[new_r][new_c] == ".":
        continue
      q.append((new_r, new_c))
  
  return cluster




def get_down_count(_map, cluster):
  R, C = len(_map), len(_map[0])
  
  end_cluster = [0]*C
  for r, c in cluster:
    end_cluster[c] = max(end_cluster[c], r)
  
  min_down = R
  for r, c in cluster:
    if r != end_cluster[c]:
      continue
    down_count = 0
    for move_r in range(r+1, R):
      if _map[move_r][c] == "x":
        break
      down_count += 1
    min_down = min(min_down, down_count)

  return min_down


def down_cluster(_map, cluster, count):
  
  for r, c in sorted(cluster, reverse=True):
    _map[r][c] = "."
    _map[r+count][c] = "x"
  return _map

def print_map(_map):
  for line in _map:
    print("".join(line))


R, C = map(int, input().split())
_map = [list(input().strip()) for _ in range(R)]
N, h_list = int(input()), list(map(int, input().split()))
print_map(solution(_map, h_list))

