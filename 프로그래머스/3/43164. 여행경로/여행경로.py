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
        
    