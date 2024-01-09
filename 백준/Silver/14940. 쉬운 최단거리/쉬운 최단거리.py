from collections import deque
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [-2] * M for _ in range(N) ]


def solution():
  global visited
  
  start = find_goal()
  bfs(start)
  convert_point()
  for line in visited:
    print(*line)
    
  
def bfs(start):
  global arr, visited, N, M
  
  q = deque([start])
  while q:
    pos = q.popleft()
    for new_p in get_nearby(pos, N, M):
      r, c = new_p
      if visited[r][c] != -2:
        continue
      if arr[r][c] == 1:
        visited[r][c] = visited[pos[0]][pos[1]] + 1
        q.append((r,c))
      else:
        visited[r][c] = 0
      
def get_nearby(point, N, M):
  dr = [1, -1, 0, 0]
  dc = [0,  0, 1, -1]

  r, c = point
  nearby = []
  for i in range(4):
    new_r = r + dr[i]
    new_c = c + dc[i]
    if new_r > N-1 or new_r < 0 or new_c > M-1 or new_c < 0:
      continue
    nearby.append((new_r, new_c))

  return nearby  

def convert_point():
  global visited, arr, N, M
  for i in range(N):
    for j in range(M):
      if visited[i][j] == -2:
        visited[i][j] = -1 if arr[i][j] == 1 else 0
  
  
def find_goal():
  global arr, visited, N, M
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 2:
        visited[i][j] = 0
        return (i,j)
        

solution()