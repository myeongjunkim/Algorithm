import sys
from collections import deque

input = sys.stdin.readline

# 8:13
"""
조건:
  - 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
  - 뱀은 처음에 오른쪽을 향한다. (0,0)
  - N은 100, 사과 K 는 100
  - 뱀의 방향 변환 횟수 L 100
  - 90도 방향을 회전
구현:
  - 시뮬레이션
  - deque 를 이용하여 뱀 구현
"""


def solution(N, apple, turn):
  direct = [(0,1), (1,0), (0,-1), (-1,0)]
  visited_apple = []
  turn = deque(turn)
  pos_r, pos_c, pos_d, time = 0,0,0,0
  snake = deque([(0,0)])
  while True:
    time += 1
    dr, dc = direct[pos_d]
    pos_r, pos_c = pos_r+dr, pos_c+dc
    
    if (pos_r, pos_c) in snake:
      return time
    if not (0<=pos_r<N and 0<=pos_c<N):
      return time

    if (pos_r, pos_c) in apple and (pos_r, pos_c) not in visited_apple:
      visited_apple.append((pos_r, pos_c))
    else:
      snake.popleft()
    snake.append((pos_r, pos_c))

    if turn and turn[0][0] == time:
      turn_t, turn_d = turn.popleft()
      if turn_d == "D":
        pos_d = pos_d+1 if pos_d != 3 else 0
      elif turn_d == "L":
        pos_d = pos_d-1 if pos_d != 0 else 3
      

def print_snake(N, snake):
  for r in range(N):
    for c in range(N):
      if (r,c) in snake:
        print(1, end="")
      else:
        print(0, end="")
    print()


# main
N, K = int(input()), int(input())
apple = [ tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K) ]
L = int(input())
turn = [  [ int(n) if n.isdigit() else n for n in  input().split() ] for _ in range(L) ]
print(solution(N, apple, turn))
