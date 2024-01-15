# 2022 KAKAO TECH INTERNSHIP

from collections import deque

"""
    조건: 
        - 정확성, 효율성, 테스트 부분점수
        - ShiftRow, Rotate 구현
        - rc 는 행렬, operations 는 액션
        - rc -> 5만 x 5만
        - operations 10만
        - 메모리 제한은 없다.        
    정확성 조건(재확인 필요):
        - 표준 100 x 100 , 최대 1000
    구현:
        - rc의 양 옆 열을 deque 에 넣고 관리
        - rc 의 가운데 파트 행들을 deque 에 넣고 관리
        
"""

def solution(rc, operations):
    R, C = len(rc), len(rc[0])
    
    middle_row = deque( deque(row[1:-1]) for row in rc   )
    left_col = deque( row[0] for row in rc )
    right_col = deque( row[C-1] for row in rc )
    
    
    for op in operations:
        if op[0] == "S":
            left_col.appendleft(left_col.pop())
            middle_row.appendleft(middle_row.pop())
            right_col.appendleft(right_col.pop())
        else:
            right_bottom = right_col.pop()
            middle_row[R-1].append(right_bottom)
            
            bottom_left = middle_row[R-1].popleft()
            left_col.append(bottom_left)
            
            right_top = left_col.popleft()
            middle_row[0].appendleft(right_top)
            
            top_right = middle_row[0].pop()
            right_col.appendleft(top_right)
            
            
            
    
    result = []
    for i in range(R):
        line = [left_col[i]] + list(middle_row[i]) + [right_col[i]]
        result.append(line)
        
    return result
    