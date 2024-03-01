from collections import deque

def solution(N, wires):
    
    def get_map(N, wires):
        _map = [ [] for _ in range(N+1) ]
        for a,b in wires:
            _map[a].append(b)
            _map[b].append(a)
        return _map
    
    def bfs(start, _map):
        visited = [False]*(N+1)
        visited[start] = True

        result = 0
        q = deque([start])
        while q:
            pos_n = q.popleft()
            result += 1
            for new_n in _map[pos_n]:
                if visited[new_n]:
                    continue
                visited[new_n] = True
                q.append(new_n)
        
        return result
    
    
    min_diff = int(1e9)
    for d_index in range(len(wires)):
        new_wires = [ wires[i] for i in range(len(wires)) if i != d_index]
        _map = get_map(N, new_wires)
        part1 = bfs(1, _map)
        part2 = N-part1
        min_diff = min(min_diff, abs(part1-part2))
    
    
    return min_diff