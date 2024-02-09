import sys

input = sys.stdin.readline

"""
조건: 
  - n 은 1만
  - 1, 2, 3 의 합으로 나타내기
구현:
  - n 은 n-1, n-2, n-3 의 경우를 더한 경우이다.
    -> 이럴 경우 중복이 생기는 이슈 발생
  
"""


def solution(cases):

  N = max(cases)
  dp = [ [0,0,0,0] for _ in range(N+4) ]
  dp[1] = [0,1,0,0]
  dp[2] = [0,0,1,0]
  dp[3] = [0,1,1,1]

  if N > 3:
    for i in range(4, N+1):
      dp[i][1] = (dp[i][1] + ( dp[i-1][2] + dp[i-1][3] )) % 1_000_000_009
      dp[i][2] = (dp[i][2] + ( dp[i-2][1] + dp[i-2][3] )) % 1_000_000_009
      dp[i][3] = (dp[i][3] + ( dp[i-3][1] + dp[i-3][2] )) % 1_000_000_009

  return [ sum(dp[c]) % 1_000_000_009 for c in cases ]
  
# main
T = int(input())
cases = [ int(input()) for _ in range(T) ]
print(*solution(cases), sep="\n")

