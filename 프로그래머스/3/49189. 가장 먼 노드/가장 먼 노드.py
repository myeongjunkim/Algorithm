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

def solution(n, edge):
    def get_map(n, edge):
        _map = [ [] for i in range(n+1) ]
        for a, b in edge:
            _map[a].append(b)
            _map[b].append(a)
        return _map
            
    
    _map = get_map(n, edge)
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
    
    return visited.count(max(visited))