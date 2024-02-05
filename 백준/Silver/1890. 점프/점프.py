import sys

input = sys.stdin.readline

"""
조건: 
  - N (4 ≤ N ≤ 100)
  - 오른쪽 또는 아래로 이동
  - 경로의 수 조사
  
구현:
  - 2차원 dp 설정
  - 각 칸마다 왼쪽에서 온 경우, 위에서 온 경우 합으로 기록
  

"""



def solution(N, _map):
  dp = [[0]*N for _ in range(N)]
  dp[0][0] = 1
  for r in range(N):
    for c in range(N):
      for pre_r in range(r):
        if r-pre_r == _map[pre_r][c]:
          dp[r][c]+= dp[pre_r][c]
  
      for pre_c in range(c):
        if c-pre_c == _map[r][pre_c]:
          dp[r][c] += dp[r][pre_c]

  return dp[-1][-1]


# main
N = int(input())
_map = [ list(map(int, input().split())) for _ in range(N) ]
print(solution(N, _map))


