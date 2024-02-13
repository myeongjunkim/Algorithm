import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

"""
조건:
  - 정점의 개수 V 는 2만
  - 간선의 개수 E 는 30만
  
구현:
  - 
"""

INF = 10*20_000

def solution(start, _map):

  dp = [INF] * len(_map)
  dp[start] = 0
  heap = [(0,start)]
  while heap:
    pos_w, pos_n = heappop(heap)

    if pos_w > dp[pos_n]:
      continue
    for new_n, new_w in _map[pos_n].items():
      if dp[new_n] > dp[pos_n] + new_w:
        dp[new_n] = dp[pos_n] + new_w
        heappush(heap, (dp[new_n], new_n))

  return dp



# main
V, E = map(int, input().split())
start = int(input())
lines = [ list(map(int, input().split())) for _ in range(E) ]
_map = [ {} for _ in range(V+1)]
for a, b, w in lines:
  try:
    _map[a][b] = min(_map[a][b], w)
  except KeyError:
    _map[a][b] = w
    
  
for n, dist in enumerate(solution(start, _map)):
  if n == 0:
    continue
  print(dist if dist!=INF else "INF")