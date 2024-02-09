import sys

input = sys.stdin.readline

"""
조건: 
  - N 은 150만
  - 상담일수 T 는 50, 급여는 1000
구현:
  - n 일이 끝났을 때 정산된 금액의 경우를 dp[n] 에 기록
  - dp 구조
    - (총 급여, 정산예정금액, 남은 일수)
  
"""


def solution(N, works):

  dp = [ 0 for _ in range(N+2) ]
  max_value = 0
  for today in range(1, N+1):
    T, P = works[today]
    max_value = max(max_value, dp[today])
    dp[today] = max(max_value, dp[today])
    if today+T <= N+1:
      dp[today+T] = max(dp[today]+P, dp[today+T])
  return max(dp)
  
# main
N = int(input())
works = [[0,0]] + [ list(map(int, input().split())) for _ in range(N) ]
print(solution(N, works))

