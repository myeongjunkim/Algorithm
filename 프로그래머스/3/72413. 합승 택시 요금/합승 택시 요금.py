# 2021 KAKAO BLIND RECRUITMENT

# 12:24 ~

"""
조건:
    - 합승을 고려한 최소 택시 비용
    - 지점은 1 ~ n, n 은 200
    - fares 배열의 각 행은 [c, d, f]
구현: 
    - 
    - 최단거리 문제, 양수 가중치이므로 다익스트라를 통한 구현
        1. 출발점 부터 각 지점까지 최단 거리 dp 를 먼저 다 구한다.
        2. 각 지점을 순회하면서 a, b 까지의 최단거리를 각 지점까지 거리에 더해보며 최소비용을 찾는다.
            - 각 지점에서 a, b 까지의 최단거리는 모든 노드의 다익스트라 dp를 통해 미리 구한다.
    
"""

from heapq import heappop, heappush

INF = int(1e9)

def solution(n, s, a, b, fares):
    _map = get_map(n, fares)
    
    dp_from_s = dijkstra(_map, s)
    dp_from_a = dijkstra(_map, a)
    dp_from_b = dijkstra(_map, b)
    
    min_w = INF
    for n in range(1, n+1):
        total_w = dp_from_s[n] + dp_from_a[n] + dp_from_b[n]
        min_w = min(total_w, min_w)
    
    return min_w



def dijkstra(_map, s):
    dp = [INF]*len(_map)
    visited = [False]*len(_map)
    
    dp[s] = 0
    heap = [ (0,s) ]
    while heap:
        pos_w, pos_n = heappop(heap)
        visited[pos_n] = True
        
        for next_w, next_n in _map[pos_n]:
            if dp[next_n] > dp[pos_n]+next_w:
                dp[next_n] = dp[pos_n]+next_w
                heappush( heap, (next_w, next_n) )
    
    return dp
    

def get_map(n, fares):
    _map = [ [] for _ in range(n+1) ]
    for n1, n2, w in fares:
        _map[n1].append((w, n2))
        _map[n2].append((w, n1))
    return _map
