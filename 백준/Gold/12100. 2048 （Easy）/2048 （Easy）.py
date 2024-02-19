import sys

input = sys.stdin.readline

# 6:38
"""
조건:
  - 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다
  - 최대 5번 이동
  - N 은 20
구현:
  - 재귀를 통한 완전 탐색으로 구현
  - 상하 좌우 이동하는 시뮬레이션 구현
    - 방향별로 숫자만 집어오누 line 생성
    - line을 순회하면서 i 와 i+1 번째 개체 동일 여부 확인
      - 동일하면 합치고 아니면 그대로
    - 이동한 라인을 이동방향에 밀착하여 업데이트
    - 모든 라인에 대하여 이동
  - 만약 시간 초과 나오면 이동전후 같을 때 스킵
"""

MAX_RESULT = 0

def solution(N, _map):
  global MAX_RESULT
  
  def back_tracking(_map, depth):
    if depth > 5:
      return
    
    left_map = move_left(N, _map)
    back_tracking(left_map, depth+1)
    
    right_map = move_right(N, _map)
    back_tracking(right_map, depth+1)

    up_map = move_up(N, _map)
    back_tracking(up_map, depth+1)
    
    down_map = move_down(N, _map)
    back_tracking(down_map, depth+1)

  back_tracking(_map, 1)
  return MAX_RESULT


def move_left(N, _map):
  global MAX_RESULT
  new_map = []
  for line in _map:
    n_line = [ n for n in line if n != 0]
    new_line = []
    i = 0
    while i < len(n_line):
      if i+1 < len(n_line) and n_line[i] == n_line[i+1]:
        new_line.append(n_line[i] * 2)
        MAX_RESULT = max(MAX_RESULT, n_line[i] * 2)
        i += 2
      else:
        new_line.append(n_line[i])
        i += 1
    new_map.append(new_line + [0]*(N - len(new_line)))
  return new_map

def move_right(N, _map):
  global MAX_RESULT
  
  new_map = []
  for line in _map:
    n_line = [ n for n in line if n != 0]
    new_line = []
    i = len(n_line) - 1
    while i >= 0:
      if i-1 >= 0 and n_line[i] == n_line[i-1]:
        new_line.append(n_line[i] * 2)
        MAX_RESULT = max(MAX_RESULT, n_line[i] * 2)
        i -= 2
      else:
        new_line.append(n_line[i])
        i -= 1
    
    new_line = new_line + [0]*(N-len(new_line))
    new_line.reverse()
    new_map.append(new_line) 
  return new_map

def move_up(N, _map):
  global MAX_RESULT
  new_map = [ [0]*N for _ in range(N) ]
  
  for c in range(N):
    n_line = [ _map[r][c] for r in range(N) if _map[r][c] != 0]
    new_line = []
    i = 0
    while i < len(n_line):
      if i+1 < len(n_line) and n_line[i] == n_line[i+1]:
        new_line.append(n_line[i] * 2)
        MAX_RESULT = max(MAX_RESULT, n_line[i] * 2)
        i += 2
      else:
        new_line.append(n_line[i])
        i += 1
    
    for r in range(len(new_line)):
      new_map[r][c] = new_line[r]
      
  return new_map

def move_down(N, _map):
  global MAX_RESULT
  new_map = [ [0]*N for _ in range(N) ]
  
  for c in range(N):
    n_line = [ _map[r][c] for r in range(N) if _map[r][c] != 0 ]
    new_line = []
    i = len(n_line) - 1
    while i >= 0:
      if i-1 >= 0 and n_line[i] == n_line[i-1]:
        new_line.append(n_line[i] * 2)
        MAX_RESULT = max(MAX_RESULT, n_line[i] * 2)
        i -= 2
      else:
        new_line.append(n_line[i])
        i -= 1

    new_line.reverse()
    r = N-1
    while new_line:
      new_map[r][c] = new_line.pop()
      r -= 1
  return new_map

def print_map(_map):
  for line in _map:
    print(line)

def get_max(_map):
  result = 0
  for line in _map:
    for n in line:
      result = max(result, n)
  return result


# main
N = int(input())
_map = [ list(map(int, input().split())) for _ in range(N) ]
MAX_RESULT = get_max(_map)
print(solution(N, _map))
