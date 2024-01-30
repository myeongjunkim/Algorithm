import sys

input = sys.stdin.readline

"""
조건: 
  - 거북이의 이동을 포함하는 가장 작은 직사각형의 넓이
  - 명령 길이는 500 이하
  
구현:
  - 상하좌우의 최대 최소 값 기록
  - 넓이 구하기
"""


def solution(case):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  d_index = 0

  max_pos = [0,0]
  min_pos = [0,0]
  x, y = 0, 0
  for c in case:
    if c in "FB":
      if c == "F":
        x += dx[d_index]
        y += dy[d_index]
      else:
        x -= dx[d_index]
        y -= dy[d_index]
      max_pos[0] = max(max_pos[0], x)
      max_pos[1] = max(max_pos[1], y)
      min_pos[0] = min(min_pos[0], x)
      min_pos[1] = min(min_pos[1], y)
    elif c == "L":
      d_index = 3 if d_index == 0 else d_index-1
    elif c == "R":
      d_index = 0 if d_index == 3  else d_index+1


  return (max_pos[0]-min_pos[0]) * (max_pos[1]-min_pos[1])




# main
N = int(input())
test_case = [ input().strip() for _ in range(N) ]
for case in test_case:
  print(solution(case))
