import sys
from collections import deque, defaultdict

input = sys.stdin.readline

"""
조건: 
  - 4개 이상 모이게 되면 제거
구현:
  - 입력을 column 형태로 받아서 큐에 저장
  - dfs 를 통해 4개 이상 있는지 전체 필드 점검
    - 각 위치를 파악해야됨
  - 4개 이상 있는 곳은 제거 후 column 평행 이동
  - count 관리
"""



def solution(_map):
  column_map = [ [line[i] for line in _map] for i in range(6) ]
  puyos = check_puyo(column_map)
  count = 0
  while puyos:
    # print(puyos)
    column_map = update_column_map(column_map, puyos)
    puyos = check_puyo(column_map)
    # print_column_map(column_map)
    count += 1
  return count



def check_puyo(column_map):
  checked = [[False]*12 for _ in range(6)]
  result = []
  for c in range(6):
    for r in range(12):
      if column_map[c][r] != "." and not checked[c][r]:
        puyo = []
        visited = [[False]*12 for _ in range(6)]
        q = deque([(c, r)])
        while q:
          pos_c, pos_r = q.popleft()
          if visited[pos_c][pos_r]:
            continue
          visited[pos_c][pos_r] = True
          puyo.append((pos_c, pos_r))
          
          for dc, dr in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_c, new_r = pos_c+dc, pos_r+dr
            if not (0<=new_c<6 and 0<=new_r<12):
              continue
            if visited[new_c][new_r]:
              continue
            if column_map[pos_c][pos_r] != column_map[new_c][new_r]:
              continue
            q.append((new_c,new_r))
            
        if len(puyo) > 3:
          result.append(puyo)
          for p_c, p_r in puyo:
            checked[p_c][p_r] = True

  return result
      

def update_column_map(column_map, puyos):
  for puyo in puyos:
    for c, r in puyo:
     column_map[c][r] = None

  for c in range(6):
    part_column = [column_map[c][r] for r in range(12) if column_map[c][r]]
    column_map[c] = ["."]*(12-len(part_column)) + part_column
    
  return column_map


def print_column_map(column_map):
  for r in range(12):
    for c in range(6):
      print(column_map[c][r], end="")
    print("")

# main
_map = [ list(input().strip()) for _ in range(12) ]
print(solution(_map))