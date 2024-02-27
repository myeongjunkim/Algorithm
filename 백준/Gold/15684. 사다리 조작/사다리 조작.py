import sys

input = sys.stdin.readline

"""
조건:
  - N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
  - 세로선 N, 가로선 H
  - (a,b) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결
  - i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 
    추가해야 하는 가로선 개수의 최솟값
구현:
  - 
"""

def solution(N,M,H, _map):

  # V = [ [ [False, False] for _ in range(H+1) ]  for _ in range(N+1) ]
  # for a, b in _map:
  #   V[b][a][1] = True
  #   V[b+1][a][0] = True

  V = [ [False]*(H+1) for _ in range(N+1)]
  for a, b in _map:
    V[b][a] = True

  result = -1
  
  def simulation(V):
    for n in range(1, N+1):
      pos_v = n
      for pos_h in range(1, H+1):
        if V[pos_v-1][pos_h]:
          pos_v -= 1
        elif V[pos_v][pos_h]:
          pos_v += 1
      if pos_v != n:
        return False
    else:
      return True
    
  def bt(depth, V):
    nonlocal result
    if result != -1 and depth >= result:
      return
    if simulation(V):
      result = depth if result == -1 else min(depth, result)
    elif depth < 3:
      for v in range(1, N):
        for h in range(1, H+1):
          if V[v-1][h] or V[v][h] or V[v+1][h]:
            continue
          V[v][h] = True
          bt(depth+1, V)
          V[v][h] = False

  bt(0, V)
  return result
  
  
# main
N, M, H = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(M) ]
print(solution(N,M,H, _map))




