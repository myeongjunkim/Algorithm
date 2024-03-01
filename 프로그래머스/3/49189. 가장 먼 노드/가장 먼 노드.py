"""
조건:
    - 가장 멀리 떨어진 노드
        최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미
    - n은 2 이상 20,000 이하
    - 1개 이상 50,000개 이하의 간선
구현:
    - 모든 노드 탐색하며 거리 기록
    - 거리 최대값과 같은 노드 개수 구하기
"""

from collections import deque
from heapq import heappush, heappop

import sys

def solution(n, edge):
    def get_map(n, edge):
        _map = [ [] for i in range(n+1) ]
        for a, b in edge:
            _map[a].append(b)
            _map[b].append(a)
        return _map

    def get_weight_map(n, edge):
        _map = [ [] for i in range(n+1) ]
        for a, b in edge:
            _map[a].append((1, b))
            _map[b].append((1, a))
        return _map
            
    def bfs(_map, start):
        visited = [0]*(n+1)
        start_n = 1
        q = deque([start_n])
        while q:
            pos_n = q.popleft()
            for new_n in _map[pos_n]:
                if new_n == start_n:
                    continue
                if visited[new_n]:
                    continue
                visited[new_n] = visited[pos_n]+1
                q.append(new_n)
        return visited
    
    def dijkstra(_map, start):
        
        dist = [sys.maxsize]*(n+1)
        dist[0] = 0
        dist[start] = 0
        heap = [ (0,start) ]
        
        while heap:
            pos_dist, pos_n = heappop(heap)
            
            if pos_dist > dist[pos_n]:
                continue
            for new_w, new_n in _map[pos_n]:
                if dist[new_n] > dist[pos_n] + new_w:
                    dist[new_n] = dist[pos_n] + new_w
                    heappush(heap, (dist[new_n], new_n))
        return dist
        
        
            
    
    
    # _map = get_map(n, edge)
    # dist = bfs(_map, 1)
    
    weight_map = get_weight_map(n, edge)
    dist = dijkstra(weight_map, 1)
    print(dist)
    
    return dist.count(max(dist))