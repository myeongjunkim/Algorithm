# 2024 KAKAO WINTER INTERNSHIP

# 2차원 리스트 언팩
# 리스트, 딕셔너리 키 지우기

"""
4:36~

조건:
    - 그래프
        - 도넛 모양(n, n), 순환고리 1개, in 1개 out 1개 
        - 막대 모양(n, n-1), -> 순환고리 x,  in 1개, out 1개 두개 다름
        - 8자 모양(2n+1, 2n+2) -> 들어가는거 두개, 나가는거 두개 노드가 한개 이상
    - 각 그래프는 여러개
    - 무관한 정점을 하나 생성한 뒤, 각 그래프의 임의의 정점 하나로 향하는 간선들 생성
    - 그래프의 간선 정보가 주어지면 
        - 생성한 정점의 번호와 
        - 정점을 생성하기 전 
            도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수 (합은 2 이상)
    - 간선정보 1 ≤ edges의 길이 ≤ 1,000,00
    - 1 ≤ a, b ≤ 1,000,000
구현:
    - 들어오는 간선이 없는 노드가 곧 추가된 노드
    - 추가된 노드 구하는 메소드
    - 추가된 노드에서 들어오는 간선 제외하는 메소드
    - 각각의 그래프 방문을 두고 순회, 출발 노드를 확인하고 순회
        - 만약 new_n 이 출발노드이면
        - 어떤 그래프인지 구분
    - 어떤 그래프인지 구분하는 메소드
예외:
    - 다 돌기 전에 다시 시작점으로 오는 경우 처리 필요
    - 혼자 있는 type 2 처리 필요
"""

from collections import defaultdict, deque

def solution(edges):
    def get_map(edges):
        _map = defaultdict(list)
        key_set, value_set, all_node_set = set(), set(), set()
        for i in range(len(edges)):
            a, b = edges[i]
            _map[a].append((b, i))
            key_set.add(a)
            value_set.add(b)
            all_node_set.add(a)
            all_node_set.add(b)
        
        add_node = 0
        for key in list(key_set-value_set):
            if len(_map[key]) >= 2:
                add_node = key
        
        return _map, add_node
        
        
        
        

    def bfs(index):
        nonlocal visited, _map, edges
        
        a, b = edges[index]
        route_count = 0
        node_set = set([b])
        
        q = deque( [ b ] )
        while q:
            pos_n = q.popleft()
            for new_n, new_index in _map[pos_n]:
                if visited[new_index]:
                    continue
                visited[new_index] = True
                q.append(new_n)
                node_set.add(new_n)
                route_count += 1
        return len(list(node_set)), route_count
    
    
    
    _map, add_node = get_map(edges)
    type1, type2, type3 = 0, 0, 0
    visited = [False]*len(edges)
    for start, index in _map[add_node]:
        node_count, route_count = bfs(index)
        if node_count == route_count:
            type1 += 1
        elif node_count > route_count:
            type2 += 1
        elif node_count < route_count:
            type3 += 1
    
    
    return [add_node, type1, type2, type3]