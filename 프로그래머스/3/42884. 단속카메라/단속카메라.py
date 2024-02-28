"""
7:26~

조건:
    - 
구현:
    - 도착 지점을 기준으로 정렬하기
    - 경로를 순회하면서
        - 이전 카메라 지점이 경로에 포함 안되어 있으면
        - 도착 지점에 카메라 설치 
예외:
    -
"""


def solution(routes):
    routes = sorted(routes, key=lambda x:x[1])
    
    camera = [ routes[0][1] ]
    for start, end in routes:
        if start<= camera[-1] <=end:
            continue
        camera.append(end)
    return len(camera)

