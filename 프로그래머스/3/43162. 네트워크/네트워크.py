"""
5:51~

조건:
    - n은 1 이상 200 이하
    - 노드는 0부터 n-1인 정수
    - computers[i][j]를 1로
구현:
    - visited = 0 값을 같은 n 길이 배열
    - 0~n-1까지 순회
        bfs 를 통한 탐색 -> 탐색한 곳에는 visited 배열에 id 값 부여
        id 는 +1
"""
from collections import deque

def solution(n, computers):
    visited = [0] * n
    id = 1
    def bfs(start_n):
        nonlocal visited, id
        q = deque([start_n])
        while q:
            pos_n = q.popleft()
            for new_n in range(n):
                if visited[new_n]:
                    continue
                if not computers[pos_n][new_n]:
                    continue
                visited[new_n] = id
                q.append(new_n)
            
    
    for node in range(n):
        if visited[node]:
            continue
        bfs(node)
        id+=1
        
    return max(visited)