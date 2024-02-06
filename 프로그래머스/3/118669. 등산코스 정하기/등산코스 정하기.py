from heapq import heappop, heappush, heapify

INF = int(1e9)

def solution(n, paths, gates, summits):
    nodes = get_nodes(n, gates, summits)
    _map = get_map(n, paths)
    return dijkstra(gates, _map, nodes)
            

def dijkstra(gates, _map, nodes):
    dp = [INF]*(len(nodes))
    result = []
    
    heap = []
    for g in gates:
        heap.append((0, g))
        dp[g] = 0
    while heap:
        pos_w, pos_n = heappop(heap)

        if pos_w > dp[pos_n]:
            continue
        if nodes[pos_n] == "s":
            result.append((pos_n, dp[pos_n]))
            continue

        for next_w, next_n in _map[pos_n]:
            if nodes[next_n] == "g":
                continue
            intensity = max(dp[pos_n], next_w)
            if dp[next_n] > intensity:
                dp[next_n] = intensity
                heappush(heap, (next_w, next_n))
        
    return min(result, key=lambda x: (x[1], x[0]))


def get_nodes(N, gates, summits):
    nodes = ["n"] * (N+1)
    for gate in gates:
        nodes[gate] = "g"
    for summit in summits:
        nodes[summit] = "s"
    return nodes


def get_map(N, paths):
    _map = [ [] for _ in range(N+1) ]    
    for n1, n2, w in paths:
        _map[n1].append((w, n2))
        _map[n2].append((w, n1))
    return _map