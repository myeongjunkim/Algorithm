# 2024 KAKAO WINTER INTERNSHIP

"""
4:04 ~ 

조건:
    - 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
    - 같으면 선물지수가 작은사람 -> 큰사람
    - 선물지수 : [이번 달까지] 준 선물의 수-받은 선물의 수
    - 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
    - friends 50, gifts 1만
    - 
구현:
    - 자료구조 문제
    - 준 선물 카운트 하는 맵 만들기
        {
            a: {a:0, b:1, c:1},
            b: {a:2, b:0, c:4},
        }
    - 두명의 선물차이 구하는 메소드
    - 선물지수 구하는 메소드
예외:
    - 
"""
from itertools import combinations

def solution(friends, gifts):
    def get_map(friends, gifts):
        _map = { a:{ b:0 for b in friends}   for a in friends}
        for line in gifts:
            a, b = line.split()
            _map[a][b] += 1
        return _map
    
    def calc_gindex(a, _map):
        give = sum(_map[a].values())
        take = sum( give_dict[a] for give_dict in _map.values() )
        return give-take
    
    def calc_result(friends, _map):
        result = { a:0 for a in friends }
        for a,b in combinations(friends, 2):
            if _map[a][b] > _map[b][a]:
                result[a]+=1
            elif _map[a][b] < _map[b][a]:
                result[b]+=1
            else:
                a_gindex = calc_gindex(a,_map)
                b_gindex = calc_gindex(b,_map)
                if a_gindex > b_gindex:
                    result[a]+=1
                elif a_gindex < b_gindex:
                    result[b]+=1
                else:
                    pass
        return result
            

    _map = get_map(friends, gifts)
    result = calc_result(friends, _map)
    return max(result.values())
