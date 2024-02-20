import sys

from heapq import heappush, heappop

input = sys.stdin.readline

"""
조건:
  - N 은 1000
  - M 은 10만
  - 양방향 연결
구현:
  - 최소비용트리 -> 프림 알고리즘 풀이
"""

def solution(N, _map):
  result = 0
  visited = [False]*(N+1)
  
  heap = [(0,1)]
  while heap:
    w, n = heappop(heap)
    if visited[n]:
      continue
    
    visited[n] = True
    result += w

    for next_w, next_n in _map[n]:
      if visited[next_n]:
        continue
      heappush(heap, (next_w, next_n))
  
  return result


# main
N, M = int(input()), int(input())
_map = [[] for _ in range(N+1)]
for _ in range(M):
  a, b, w = map(int, input().split())
  if a != b:
    _map[a].append((w,b))
    _map[b].append((w,a))
print(solution(N, _map))
