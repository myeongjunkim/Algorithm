# dfs
graph = [ # n 번 노드의 인접 노드 그래프
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 재귀로 구현
visited=[False] * 9 # node 개수
def dfs(graph, v, visited):
    visited[v] = True
    # v 필요에 따라 리스트에 저장 & 사용
    print(v)
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)






# 스택으로 구현 가능
visited=[False] * 9 # node 개수
def dfs_for_stack(graph, v, visited):
    stack = [v]
    while stack:
        node = stack[-1]
        if not visited[node]:
            print(node)
            visited[node] = True

        ending = True
        for nearby in graph[node]:
            if not visited[nearby]:
                stack.append(nearby)
                ending=False
                break
        if ending:
            # print(stack)
            # print("pop",stack.pop())
            stack.pop()

# dfs_for_stack(graph, 1, visited)
dfs(graph, 1, visited)