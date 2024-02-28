"""
조건:
    - 방문하는 공항 경로를 배열에 담아 return 
    - 주어진 공항 수는 3개 이상 10,000개 이하
    - 가능한 경로가 2개 이상일 경우 사전순 우선 리턴
    - 항상 "ICN" 공항에서 출발합니다.
구현:
    - 도시 리스트 구하고 사전순 정렬
    - depth 가 도시 숫자면 리턴
    - visited, _map
예외:
    - 모든 노드를 다 순회하는 것이 목적이 아니다. 즉 visited 관리를 하는 백트래킹 문제이다.
"""

from collections import defaultdict

def solution(tickets):
    def get_map(tickets):
        _map = defaultdict(list)
        for i in range(len(tickets)):
            a, b = tickets[i]
            _map[a].append((b, i))
        for city in _map:
            _map[city].sort() 
        return _map

    
    _map = get_map(tickets)
    dist = len(tickets)+1
    visited = [False]*len(tickets)
    result = []
    def dfs(city, path):
        nonlocal result, visited, dist, _map
        if result:
            return
        if len(path) == dist:
            result = path.copy()
            return
        for new_c, new_i in _map[city]:
            if visited[new_i]:
                continue
            visited[new_i] = True
            path.append(new_c)
            dfs(new_c, path)
            path.pop()
            visited[new_i] = False
    
    
    dfs("ICN", ["ICN"])
    return result
        
    