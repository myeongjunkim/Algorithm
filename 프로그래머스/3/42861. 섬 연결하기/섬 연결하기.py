"""
7:16 ~

조건:
    - 섬의 개수 n은 1 이상 100 이하
    - costs의 길이는 ((n-1) * n) / 2이하
구현:
    - 최소신장 트리
    - 가장 작은 거리만 선택해서 구한다.
예외:
    - 

"""

from heapq import heapify, heappush, heappop

def solution(N, costs):
        
    _map = [[] for _ in range(N)]
    for a, b, w in costs:
        _map[a].append((w,b))
        _map[b].append((w,a))
        
    
    result = 0
    visited = [False] * N
    heap = [(0,0)]
    while heap:
        w, n = heappop(heap)
        if visited[n]:
            continue
        visited[n] = True
        result += w
        
        for new_w, new_n in _map[n]:
            if visited[new_n]:
                continue
            heappush(heap, (new_w, new_n))
            
    
    return result