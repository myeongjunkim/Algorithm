import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

"""
조건:
  - 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
  - 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
  - N×N인 도시 0은 빈 칸, 1은 집, 2는 치킨집이다.
  - 도시의 치킨 거리가 가장 작게
  - N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
  - 집의 개수는 2N개를 넘지 않음
  - 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
구현:
  - 치킨집 좌표중 M 개 선택
  - bfs 로 각 집의 치킨거리 구하기 ( 치킨거리 = 이동거리 )
  - 도시의 치킨거리합을 result 에 추가
  - min 값 리턴
  
"""

def solution(N,M, _map):
  def get_chicken_points():
    points = []
    for r in range(N):
      for c in range(N):
        if _map[r][c] == 2:
          points.append((r,c))
    return points
  def get_house_points():
    points = []
    for r in range(N):
      for c in range(N):
        if _map[r][c] == 1:
          points.append((r,c))
    return points
  def bfs(start):
    r, c = start
    d = 0
    visited = [ [False]*N for _ in range(N) ]
    visited[r][c] = True

    q = deque([ (r,c,d) ])
    while q:
      r, c, d = q.popleft()
      for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_r, new_c = r+dr, c+dc
        new_d = d+1
        if not (0<=new_r<N and 0<=new_c<N):
          continue
        if visited[new_r][new_c]:
          continue
        if _map[new_r][new_c] == 2:
          return new_d
        q.append((new_r, new_c, new_d))
        visited[new_r][new_c] = True
        
    return -1
  def get_sum_dist():
    sum_dist = 0
    for r in range(N):
      for c in range(N):
        if _map[r][c] == 1:
          sum_dist += bfs((r,c))
    return sum_dist
  def calc_dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
  
  all_dist = []
  chicken_points = get_chicken_points()
  house_points = get_house_points()
  # for case in combinations(chicken_points, len(chicken_points)-M):
  #   for r, c in case:
  #     _map[r][c] = 0
  #   sum_dist = get_sum_dist()
  #   all_dist.append(sum_dist)
  #   for r, c in case:
  #     _map[r][c] = 2


  
  for case in combinations(chicken_points, M):
    sum_dist = 0
    for house in house_points:    
      dists =  [calc_dist(chicken, house) for chicken in case]
      sum_dist += min(dists)
    all_dist.append(sum_dist)

  
  return min(all_dist)

# main
N, M= map(int, input().split())
_map = [ list(map(int, input().split()))  for _ in range(N) ]
print(solution(N,M, _map))




