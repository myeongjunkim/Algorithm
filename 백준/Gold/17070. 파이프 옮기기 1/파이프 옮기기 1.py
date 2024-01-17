import sys

input = sys.stdin.readline

"""
조건: 
  - N x N // 3 < N < 16
  - [0][0] [0][1] 에서 출발
  - 벽이 있다.
  
구현:
  - N 이 작다. dp? 그렇기에는 벽이 존재
  - 그래프 이론
  - 파이프 끝 요소 nearby 찾기
  - 
  
"""

def solution(house):
  
  pipe =  (0,1,0)
  if house[0][2] == 1 or house[-1][-1] == 1:
    return
  dfs(pipe, house)
  

def dfs(pipe, house):
  global count
  N = len(house)
  r, c, dir = pipe
  if r == N-1 and c == N-1:
    count += 1
    return
    
  if ( r+1 < N 
    and c+1 < N 
    and not house[r+1][c+1] and not house[r][c+1] and not house[r+1][c]
    ):
    dfs((r+1, c+1, 2), house)
  if r+1 < N and house[r+1][c] == 0 and dir != 0:
    dfs((r+1, c, 1), house)
  if c+1 < N and house[r][c+1] == 0 and dir != 1:
    dfs((r, c+1, 0), house)
    

# main
N = int(input())
house = [ list(map(int, input().split())) for _ in range(N) ] 

count = 0
solution(house)
print(count)

      