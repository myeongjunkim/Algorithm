import sys
from collections import deque
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건: 
 - 정점의 개수 : 1만개
 - 간선의 개수: 10만개
 - 가중치 : 절대값 100만
구현:
 - 각 노드 별 연결된 노드와 가중치를 맵에 기록
  - node_map example
    #node: [{연결 node: 가중치}, ]
    {
      1: [{2: 1}, {3: 3}],
      2: [{1: 1}, {3: 2}],
      3: [{1: 3}, {2, 2}]
    }
 - 노드 방문 리스트 생성
 - 모든 정점을 연결하는 경우 체크 ( bfs or dfs )
 - 경우별로 비용을 다 더한 후 min 값 없데이트

"""
min_value = sys.maxsize

def solution():
  V, E = map(int, input().split())
  node_map = {v:[] for v in range(1,V+1)}
  for _ in range(E):
    node1, node2, weight = map(int, input().split())
    node_map[node1].append((node2, weight))
    node_map[node2].append((node1, weight))

  for node in node_map:
    node_map[node] = sorted(node_map[node], key=lambda x: x[1], reverse=True)

  visited = [True] + [False for _ in range(V)]
  heap = [(0, 1)] # weight, node
  heapq.heapify(heap)
  result = 0
  while heap:
    weight, pos = heapq.heappop(heap)
    if visited[pos]:
      continue
    visited[pos] = True
    result += weight
    for n, w in node_map[pos]:
      if not visited[n]:
        heapq.heappush(heap, (w,n))


  global min_value
  if all(visited):
    min_value = min(min_value, result)
      

solution()
print(min_value)
      