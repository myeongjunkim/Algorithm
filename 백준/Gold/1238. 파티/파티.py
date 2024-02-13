import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

"""
조건:
  - N 은 1000
  - M 은 1만
  - 비용 최대값은 100
  - 단방향 도로
  
구현:
  - X 를 시작점으로 하는 다익스트라 값
  - N명의 학생 집부터 X 까지 다익스트라 값
"""

def dijkstra(start, _map):
  dist = [sys.maxsize] * (N+1)
  dist[start] = 0
  
  heap = [(0, start)]
  while heap:
    pos_dist, pos_n = heappop(heap)
  
    if pos_dist > dist[pos_n]:
      continue
    for new_dist, new_n in _map[pos_n]:
      if dist[new_n] > dist[pos_n] + new_dist:
        dist[new_n] = dist[pos_n] + new_dist
        heappush(heap, (dist[new_n], new_n) )
  
  return dist


def solution(X, _map):
  dist_from_x = dijkstra(X, _map)
  max_dist = 0
  for n in range(1, len(_map)):
    dist_from_n = dijkstra(n, _map)
    max_dist = max(max_dist, dist_from_n[X] + dist_from_x[n])
  return max_dist


# main
N, M, X = map(int, input().split())
_map = [ [] for _ in range(N+1)]
for _ in range(M):
  a,b,w = map(int, input().split())
  _map[a].append((w, b))
  
print(solution(X, _map))