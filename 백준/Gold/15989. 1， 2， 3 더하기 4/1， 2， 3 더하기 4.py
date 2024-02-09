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
  dp = [ 1 for _ in range(N+1) ]

  for i in range(2, N+1):
    dp[i] += dp[i-2]
  for i in range(3, N+1):
    dp[i] += dp[i-3]

  return [ dp[c] for c in cases ]

# main
T = int(input())
cases = [ int(input()) for _ in range(T) ]
print(*solution(cases), sep="\n")

