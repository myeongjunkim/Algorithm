import sys

input = sys.stdin.readline

"""
조건:
  - N, M 은 20
  - _map 이 0 이면 _map에 주사위 바닥수 복사
  - 주사위 바닥이 0 이면 _map에 써있는 수 주사위에 복사
  - 상단에 쓰여 있는 값 출력
구현:
  - 주사위 자료구조 정하기
  - roll 함수 구현
  - 현재 위치 관리
  - 칸 복사 구현
    주사위칸, _map 칸
  - result 에 dice[0] 더하기
  - 바깥으로 나갈 경우
  
"""

def solution(N,M, x,y, _map, command):
  def roll_right(dice):
    dice[0], dice[1], dice[5], dice[2] = dice[2], dice[0], dice[1], dice[5]
    return dice
  def roll_left(dice):
    dice[0], dice[1], dice[5], dice[2] = dice[1], dice[5], dice[2], dice[0]
    return dice
  def roll_up(dice):
    dice[0], dice[3], dice[5], dice[4] = dice[4], dice[0], dice[3], dice[5]
    return dice
  def roll_down(dice):
    dice[0], dice[3], dice[5], dice[4] = dice[3], dice[5], dice[4], dice[0]
    return dice

  result = []

  dice = [0,0,0,0,0,0]  # 위(0), 동(1), 서(2), 북(3), 남(4), 밑(5)
  pos_r, pos_c = x, y
  for cmd in command:
    if cmd == 1:
      if pos_c+1>=M:
        continue
      pos_c += 1
      dice = roll_right(dice)
    elif cmd == 2:
      if pos_c-1<0:
        continue
      pos_c -= 1
      dice = roll_left(dice)
    elif cmd == 3:
      if pos_r-1<0:
        continue
      pos_r -= 1
      dice = roll_up(dice)
    elif cmd == 4:
      if pos_r+1>=N:  
        continue
      pos_r += 1
      dice = roll_down(dice)
    
    
    if _map[pos_r][pos_c] == 0:
      _map[pos_r][pos_c] = dice[5]
    else:
      dice[5] = _map[pos_r][pos_c]
      _map[pos_r][pos_c] = 0

    result.append(dice[0])
  
  return result

# main

N,M, x,y, K = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
print(*solution(N,M, x,y, _map, command), sep="\n")
