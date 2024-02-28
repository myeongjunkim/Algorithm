"""
6:54 ~ 
조건:
    - 1명 이상 50,000명 이하입니다.
    - 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지
    - 40kg 이상 240kg 이하입니다
    - 최대 2명씩 
구현: 
    - 정렬해서 q 에 넣기
    - 남아있는 사람중 가장 무거운사람이 먼저 타고 가벼운 사람이 들어갈 수 있을 만큼 들어가기
    - 배 카운트 증가
예외:
    - 1명인 경우
"""

from collections import deque

def solution(people, limit):
    result = 0
    q = deque(sorted(people))
    while q:
        status = q.pop()
        if q and status+q[0] <= limit:
            status += q.popleft()
        result += 1
        
    return result