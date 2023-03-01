import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def execute():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for __ in range(N+1)]
        for ___ in range(M):
            v1, v2 = map(int, input().split())
            graph[v1].append(v2)
        
        res = []
        res.append(get_domino(graph))

    for r in res:
        print(r)



def dfs(graph, v, visited, set_append: set):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited, set_append)
        else:
            set_append.discard(node)

def get_domino(graph) -> int:
    visited = [False] * len(graph)
    set_append = set()
    for i in range(1, len(graph)):
        if not visited[i]:
            set_append.add(i)
            dfs(graph, i, visited, set_append)
        
    return len(set_append)


execute()