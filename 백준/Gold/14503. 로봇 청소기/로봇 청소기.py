import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

"""
조건:
  - 3<= N, M <=50
  - 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다
  이동:
  - 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
  - 4칸 중 청소되지 않은 빈 칸이 없는 경우, 
    - 바라보는 방향을 유지한 채로 한 칸 후진
    - 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
  - 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    - 반시계 방향으로 90 회전
    - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
  - 방향 0은 북, 1은 동, 2는 남, 3은 서
  
구현:
  - 
  
  
"""

def solution(robot, N, M, _map):
  def turn(d):
    return (d+3)%4
    
  direct = [(-1,0), (0,1), (1,0), (0,-1)]
  visited = [ [False]*M for _ in range(N) ] 
  result = 0
  
  r, c, d = robot
  while True:
    visited[r][c] = True

    is_there = False
    new_r, new_c, new_d = r, c, d
    for _ in range(4):
      new_d = turn(new_d)
      dr, dc = direct[new_d]
      new_r, new_c = r+dr, c+dc
      if not (0<=new_r<N and 0<=new_c<M) or _map[new_r][new_c] != 0:
        continue
      if visited[new_r][new_c]:
        continue
      is_there = True
      break

    
    if is_there:
      r, c, d = new_r, new_c, new_d
    else:
      dr, dc = direct[d]
      new_r, new_c = r-dr, c-dc
      if not (0<=new_r<N and 0<=new_c<M) or _map[new_r][new_c] != 0:
        result = 0
        for r in range(N):
          for c in range(M):
            if visited[r][c]:
              result +=1
        return result
      r, c = new_r, new_c
    
  
# main

N, M = map(int, input().split())
robot = list(map(int, input().split()))
_map = [ list(map(int, input().split())) for _ in range(N) ]
print(solution(robot,N,M,_map))
