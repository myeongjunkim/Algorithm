import sys
from collections import deque
input = sys.stdin.readline

"""
조건:
  - 사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣고, 빨간 구슬을 구멍으로 빼내는 게임
  - 왼, 오, 위, 아래 기울이기
  - 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1
  - N, M (3 ≤ N, M ≤ 10)
구현:
  - R visited 와 B
"""

def solution(R, C, _map):
  def get_R_B_pos():
    Rr, Rc, Br, Bc = 0,0,0,0
    for r in range(R):
      for c in range(C):
        if _map[r][c] == "R":
          Rr, Rc = r,c
        if _map[r][c] == "B":
          Br, Bc = r,c
    return Rr, Rc, Br, Bc
  def move_pos(r,c, dr,dc):
    move_count = 0
    while _map[r+dr][c+dc] != "#" and _map[r+dr][c+dc] != "O":
      r, c = r+dr, c+dc
      move_count += 1
    return (r,c, move_count)
  
  Rr, Rc, Br, Bc = get_R_B_pos()
  visited = [ [ [ [0 for _ in range(C)] 
       for _ in range(R)] 
     for _ in range(C)] 
    for _ in range(R)
  ]

  visited[Rr][Rc][Br][Bc] = True
  q = deque([ (Rr, Rc, Br, Bc, int(0)) ])
  while q:
    Rr, Rc, Br, Bc, depth = q.popleft()
    if depth >= 10:
      return -1
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
      new_Rr,new_Rc, R_move_count = move_pos(Rr,Rc, dr,dc)
      new_Br,new_Bc, B_move_count = move_pos(Br,Bc, dr,dc)
      if _map[new_Br+dr][new_Bc+dc] == "O":
        continue
      if (new_Rr,new_Rc) == (new_Br,new_Bc):
        if R_move_count > B_move_count:
          new_Rr -= dr
          new_Rc -= dc
        else:
          new_Br -= dr
          new_Bc -= dc
      if _map[new_Rr+dr][new_Rc+dc] == "O":
        return depth+1
      if visited[new_Rr][new_Rc][new_Br][new_Bc]:
        continue
      visited[new_Rr][new_Rc][new_Br][new_Bc] = True
      q.append( (new_Rr,new_Rc,new_Br,new_Bc, depth+1) )
    
  return -1

# main
N, M = map(int, input().split())
_map = [ list(input().strip()) for _ in range(N) ]
print(solution(N, M, _map))
