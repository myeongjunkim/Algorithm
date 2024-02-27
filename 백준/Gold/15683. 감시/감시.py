import sys

input = sys.stdin.readline

"""
조건:
  - CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시
  - 전은 항상 90도 방향으로 
  - 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다
  - CCTV는 CCTV를 통과할 수 있다
  - CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기
  - (1 ≤ N, M ≤ 8)
  - CCTV의 최대 개수는 8개를 넘지 않는
구현:
  - 브루트포스
  - check_zero(_map) 함수 구현
  - 모든 cctv 에 대하여 4 방향 회전시 시야각 # 표시 하는 함수 구현
  - 0 북, 1동, 2남, 3서
  - cctv = [ num, r, c ]
"""

def solution(N,M, _map):
  def get_cctv(_map):
    result = []
    for r in range(N):
      for c in range(M):
        if 0 <_map[r][c] < 6:
          result.append( [ _map[r][c], r, c ] )
    return result
  def check_zero(_map):
    result = 0
    for r in range(N):
      for c in range(M):
        if _map[r][c] == 0:
          result += 1
    return result
  def update_map(_map, cctv, d):
    n, r, c = cctv
    if n == 1:
      update_line(_map, r, c, d)
    elif n == 2:
      if d%2 == 0:
        update_line(_map, r, c, 0)
        update_line(_map, r, c, 2)
      else:
        update_line(_map, r, c, 1)
        update_line(_map, r, c, 3)
    elif n == 3:
      update_line(_map, r, c, d)
      update_line(_map, r, c, (d+1)%4)
    elif n == 4:
      update_line(_map, r, c, d)
      update_line(_map, r, c, (d-1+4)%4)
      update_line(_map, r, c, (d+1)%4)
    elif n == 5:
      for i in range(4):
        update_line(_map, r, c, i)
  
  def update_line(_map, r, c, d):
    if d == 0:
      for new_r in range(r, -1, -1):
        if _map[new_r][c] == 0:
          _map[new_r][c] = 9
        elif _map[new_r][c] == 6:
          break
    elif d == 1:
      for new_c in range(c, M):
        if _map[r][new_c] == 0:
          _map[r][new_c] = 9
        elif _map[r][new_c] == 6:
          break
    elif d == 2:
      for new_r in range(r, N):
        if _map[new_r][c] == 0:
          _map[new_r][c] = 9
        elif _map[new_r][c] == 6:
          break
    elif d == 3:
      for new_c in range(c, -1, -1):
        if _map[r][new_c] == 0:
          _map[r][new_c] = 9
        elif _map[r][new_c] == 6:
          break
  def clear_map(_map):
    for r in range(N):
      for c in range(M):
        if _map[r][c] == 9:
          _map[r][c] = 0
  def print_map(_map):
    for line in _map:
      print(line)

  result = N*M
  def bt(depth, _map, cctv_list):
    nonlocal result
    if depth >= len(cctv_list):
      zero_count = check_zero(_map)
      result = min(result, zero_count)
      return
    for d in range(4):
      new_map = [ line[:] for line in _map]
      update_map(new_map, cctv_list[depth], d)
      bt(depth+1,new_map, cctv_list)

  
  cctv_list = get_cctv(_map)
  bt(0, _map, cctv_list)


  
  return result
  

  
  
  
# main
N, M = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(N) ]
print(solution(N,M, _map))




