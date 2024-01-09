"""
설명:
    - 기존 메뉴를 조합하여 코스요리 형태로 구성
    - 최소 2가지 이상으로 구성
    - 최소 2명 이상의 주문건 메뉴로 구성
조건:
    - orders: 이전 주문 내역 ( 2~20 개, 각 2~10 길이 )
    - course: 코스형태로 구성 가능한 메뉴수 ( 각 2~10 )
    - result: 코스형태, 오름차순 알파벳
구현:
    1. course 순회 c
    2. c 개만큼 뽑아왔을 때 카운팅 하는 맵 업데이트
    3. 맵에서 2 이상인 경우만 모으기
    -> 시간복잡도는 크지만(combi_order(n^2) * orders(n) * course(n)) 
        n의 크기가 작으므로 가능여부 판단.
"""

from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        course_map = {}
        for order in orders:
            for case in combinations(order, c):
                key = "".join(sorted(list(case)))
                if key not in course_map:
                    course_map[key] = 1
                else:
                    course_map[key] += 1
        
        
        answer_part = []
        max_count = 1
        for key, count in course_map.items():
            if count < 2:
                pass
            elif count > max_count:
                max_count = count
                answer_part = [key]
            elif count == max_count:
                answer_part.append(key)
        answer.extend(answer_part)
            
    answer.sort()
    return answer



