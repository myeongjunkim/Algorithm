"""
이긴 + 진 합이 n-1 인 경우
"""

from collections import deque

def solution(N, results):
    def get_map(N, results):
        _map = [ {"w": [], "l":[]} for i in range(N+1) ]
        for a,b in results:
            _map[a]["w"].append(b)
            _map[b]["l"].append(a)
        return _map         

    def bfs(_map, start, r):
        visited = [False]*(N+1)
        visited[start] = True
        q = deque([start])
        result = 0
        while q:
            pos_n = q.popleft()
            for new_n in _map[pos_n][r]:
                if visited[new_n]:
                    continue
                visited[new_n] = True
                q.append(new_n)
                result += 1
        return result
    
    
    _map = get_map(N, results)
    result = 0
    for n in range(1, N+1):
        if bfs(_map, n, "w") + bfs(_map, n, "l") == N-1:
            result += 1
    
    return result