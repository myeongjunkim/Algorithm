import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

"""
조건:
  - N 은 100
  - 간선 m 은 10만

구현:
  - 
"""



def solution(N, _map):
  for i in range(1, N+1):
    print(*dijkstra(i, _map))
  

def dijkstra(start, _map):
  dist = [sys.maxsize]*len(_map)
  dist[start] = 0
  heap=[(0,start)]
  while heap:
    pos_dist, pos_n = heappop(heap)
    if pos_dist > dist[pos_n]:
      continue
    for new_w, new_n in _map[pos_n]:
      if dist[new_n] > dist[pos_n]+new_w:
        dist[new_n] = dist[pos_n]+new_w
        heappush(heap, (dist[new_n], new_n) )

  result = []
  for d in dist[1:]:
    if d == sys.maxsize:
      result.append(0)
    else:
      result.append(d)
  return result

# main
N, m = int(input()), int(input())
_map = [ [] for _ in range(N+1) ]
for _ in range(m):
  a, b, w = map(int, input().split())
  _map[a].append((w,b))
solution(N, _map)