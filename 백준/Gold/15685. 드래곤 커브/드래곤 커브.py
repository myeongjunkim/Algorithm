import sys

input = sys.stdin.readline

"""
조건:
  - 격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만
  -  0 ≤ g ≤ 10
구현:
  - create_curve(x, y, d, g)
    - turn(curve) 함수
      - curve[-1] 기준 회전
      - curve+new_curve 리턴
    - 최종 curve 리턴
  - check_square(curve)
    100x100 완탐 확인
"""

def solution(N, _map):
  def create_curve(x, y, d, g):
    direct = [(1,0), (0,-1), (-1,0), (0,1)]
    dx, dy = direct[d]
    curve = [ (x,y), (x+dx,y+dy) ]
    for _ in range(g):
      curve = turn(curve)
    return curve
    
  def turn(curve):
    center_x, center_y = curve[-1]
    new_curve = []
    for x, y in reversed(curve):
      dx, dy = x-center_x, y-center_y
      new_point = (center_x-dy, center_y+dx)
      new_curve.append(new_point)
    return curve + new_curve[1:]

  def check_square(visited):
    result = 0
    for x in range(100):
      for y in range(100):
        if visited[x][y] and visited[x+1][y] and visited[x][y+1] and visited[x+1][y+1]:
          result += 1  
    return result
  
  visited = [ [False]*101 for _ in range(101) ]
  for x, y, d, g in _map:
    curve = create_curve(x, y, d, g)
    for x, y in curve:
      visited[x][y] = True

  return check_square(visited)
  
# main
N = int(input())
_map = [ list(map(int, input().split()))  for _ in range(N) ]
print(solution(N, _map))




