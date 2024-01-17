import sys

input = sys.stdin.readline

"""
조건: 
  - N x N // 3 < N < 16
  - [0][0] [0][1] 에서 출발
  - 벽이 있다.
  
구현:
  - dp 
  - 각 포인트별 (가로, 세로, 대각선) 을 통해 도달할 수 있는 경우 기록
  - 상단 혹은 좌측이 1이면 대각선으로 도달 x
  - 위에서부터 왼-위 껍질로 dp 채우기
    - 이전 위치에서 방향이 맞는 것만 더하기
  
"""

def solution(house):
  
  N = len(house)
  dp = [ [ [0]*3 for _ in range(N) ] for _ in range(N) ]
  for i in range(1,N):
    if house[0][i]:
      break
    dp[0][i][0] = 1
    

  for i in range(1, N):
    for c in range(i, N):
      if house[i][c] == 1:
        continue
      dp[i][c][0] = dp[i][c-1][0] + dp[i][c-1][2] # 가로 + 대각선
      dp[i][c][1] = dp[i-1][c][1] + dp[i-1][c][2] # 세로 + 대각선
      dp[i][c][2] = sum(dp[i-1][c-1]) if not house[i-1][c] and not house[i][c-1] else 0

    for r in range(i+1, N):
      if house[r][i] == 1:
        continue
      dp[r][i][0] = dp[r][i-1][0] + dp[r][i-1][2] # 가로 + 대각선
      dp[r][i][1] = dp[r-1][i][1] + dp[r-1][i][2] # 세로 + 대각선
      dp[r][i][2] = sum(dp[r-1][i-1]) if not house[r-1][i] and not house[r][i-1] else 0

  # for line in dp:
  #   print(line)

  return sum(dp[N-1][N-1])
    
  

# main
N = int(input())
house = [ list(map(int, input().split())) for _ in range(N) ] 
print(solution(house))

      