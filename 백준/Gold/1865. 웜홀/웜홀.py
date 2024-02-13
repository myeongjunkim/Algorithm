import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

"""
조건:
  - 지점 N 은 500, 도로 M 은 2500, 웜홀 W 는 200
  - 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 
  - 단 도로는 방향이 없으며 웜홀은 방향이 있다.

구현:
  - 벨만포드 알고리즘을 통해 모든 지점의 최단거리를 찾는다.
  - 최단거리가 음수인 경우가 있다면 YES 를 반환한다.
"""



def solution(N, _map):
  dist = BF(N, _map)
  if not dist:
    return "YES"
  return "NO"


def BF(N, _map):
  dist = [sys.maxsize]*(N+1)
  for i in range(N):
    for a, b, w in _map:
      if dist[b] > dist[a] + w:
        dist[b] = dist[a] + w
        if i ==N-1:
          return []
  return dist

# main
T = int(input())
T_cases = []
for _ in range(T):
  N, M, W = map(int, input().split())
  _map= []
  for _ in range(M):
    a, b, w = map(int, input().split())
    _map.append((a, b, w))
    _map.append((b, a, w))
  for _ in range(W):
    a, b, w = map(int, input().split())
    _map.append((a, b, -w))
  T_cases.append((N, _map))

for N, _map in T_cases:
  print(solution(N, _map))