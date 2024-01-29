# 2022 KAKAO BLIND RECRUITMENT

# 5:42 ~ 

"""
조건:
    - 모은 양의 수보다 모은늑대의 수가 같거나 많아지면 안됨
    - 양을 모아서 다시 루트 노드로 오는 것을 목표
    - 주어진 그래프에서 모을 수 있는 양의 최대값
    - 노드는 17 개 이하, 이진트리 
    - edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태
구현:
    - 백트래킹
        - 갈수 있는 노드 나열
        - 각 노드로 갔을 때 양의 개수 max 값 업데이트
        - 재귀
        
"""

MAX_RESULT = 0

def solution(info, edges):
    global MAX_RESULT
    
    visited = [False] * 17
    _map = [ [] for i in range(17)]
    for ed in edges:
        start, end = ed
        _map[start].append(end)
    
    back_track(info, _map, visited, 0, [])
    
    return MAX_RESULT

def back_track(info, _map, visited, pos, nearby):
    global MAX_RESULT
    
    visited[pos] = True
    S, W = get_S_and_W(info, visited)
    if S<= W:
        return
    MAX_RESULT = max(S, MAX_RESULT)
    
    
    nearby += _map[pos]
    for new_pos in nearby:
        if S <= W+info[new_pos]:
            continue
        back_track(info, _map, visited.copy(), new_pos, list(set(nearby)-set([new_pos])) )
    return

def get_S_and_W(info, visited):
    S, W = 0, 0
    for i in range(17):
        if not visited[i]:
            continue
        if info[i] == 0:
            S += 1
        else:
            W += 1
    return S, W
        