import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
조건: 
  - 통로의 세로 가로 N M : 100 이하
  - 쓰레기 개수 K : N*M 이하
  
구현:
  - 모든 좌표 돌면서 dfs 로 탐색
  - dfs 는 탐색 가능 좌표가 나올 때마다 global count 에 1 씩 추가
  - 좌표 하나 돌 때마다 global count 값으로 max_count 업데이트
  - global count = 0 초기화
"""

def solution(trash_map, N, M):
  global count

  max_count = 0
  for r in range(N):
    for c in range(M):
      dfs((r,c), trash_map, N, M)
      max_count = max(max_count, count)
      count = 0
  
  return max_count


def dfs(pos, trash_map, N, M):
  global visited, count

  r, c = pos
  if visited[r][c] or trash_map[r][c] == 0:
    return

  visited[r][c] = True
  count += 1
  
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]

  for i in range(4):
    new_r = r + dr[i]
    new_c = c + dc[i]
    if (new_r< N and new_r >= 0 and new_c < M and  new_c >= 0
        and not visited[new_r][new_c] and trash_map[new_r][new_c]):
        dfs((new_r, new_c), trash_map, N, M)
      
  


# main
N, M, K = map(int, input().split())
trash_rc = [ tuple(map(int, input().split()))  for _ in range(K) ]
trash_map =[ [0]*M for _ in range(N) ]
visited = [ [False]*M for _ in range(N) ]
count = 0
for r, c in trash_rc:
  trash_map[r-1][c-1] = 1
print(solution(trash_map, N, M))


      