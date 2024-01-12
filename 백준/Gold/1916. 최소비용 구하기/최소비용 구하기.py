import sys
import heapq

input = sys.stdin.readline

"""
조건: 
  - N 개의 도시 1000개
  - M 개의 버스 10만개
구현:
  - 출발 도착 비용 버스 맵
  - heap 생성 이후 출발점 넣기
  - 출발점부터 모든 노드까지의 거리 업데이트 (다익스트라)
"""



def solution():
  N, M = int(input()), int(input())
  node_map = [[] for _ in range(N+1)]
  weights = [sys.maxsize] * (N+1)
  visited = [False] * (N+1)
  for _ in range(M):
    start, end, weight = map(int, input().split())
    node_map[start].append((weight, end))
  START, GOAL = map(int, input().split())

  weights[START] = 0
  heap = [(0, START)]
  while heap:
    weight, pos = heapq.heappop(heap)
    visited[pos] = True
    
    if weight > weights[pos]:
      continue
    for w, n in node_map[pos]:
      if not visited[n] and weights[n] > weight+w:
        weights[n] = weight+w
        heapq.heappush(heap, (weight+w, n))
    
  
  print(weights[GOAL])  

solution()

      