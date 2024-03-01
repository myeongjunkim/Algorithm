"""
5:00 ~ 

조건:
    - 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
    - 지형이 2개 이상으로 분리된 경우도 없습니다.
    - 완전히 포함되는 경우 또한 없습니다.
    - x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
    - rectangle 개수는 1~4
    - rectangle [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
    - 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수
    - charcterX, charcterY는 1 이상 50 이하인 자연수
    - itemX, itemY는 1 이상 50 이하인 자연수
구현:
    - 항상 반시계방향으로 회전
    - item 좌표와 같아지면 거리 체크 후 원점 도착까지 진행하여 거리 체크
    - move(point) 메소드 구현
        - 다음 좌표 리턴
        - 직사각형의 꼭지점이면 다른 변으로
        - 교점이면 다른 변으로
    - check(point)
        - 출발 사각형 및 출발 라인 리턴
예외:
    - 
"""

def solution(rectangle, characterX, characterY, itemX, itemY):
    def check(current, rectangle):
        result = []
        point_x, point_y = current
        for i in range(len(rectangle)):
            x1, y1, x2, y2 = rectangle[i]
            if y1 == point_y and x1<=point_x<x2:
                result.append(0)
            if x2 == point_x and y1<=point_y<y2:
                result.append(1)
            if y2 == point_y and x1<point_x<=x2:
                result.append(2)
            if x1 == point_x and y1<point_y<=y2:
                result.append(3)
        
        # 교점일 경우 len(result) == 2 
        # l_index 에 우선순위 존재 0 -> 3 -> 2 -> 1 -> 0 -> ,,,
        return max(result) if set(result) == {0, 3} else min(result)
                
    
    def move(point, l_index):
        direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
        dx, dy = direct[l_index]
        x, y = point
        return (x+dx, y+dy)
    
    
    start = (characterX, characterY)
    item = (itemX, itemY)
    current = (characterX, characterY)
    start_d, item_d = 0, 0
    while True:
        l_index = check(current, rectangle)
        current = move(current, l_index)
        start_d += 1
        if current == item:
            item_d = start_d
        if current == start:
            break

    return min(start_d-item_d, item_d)
    
