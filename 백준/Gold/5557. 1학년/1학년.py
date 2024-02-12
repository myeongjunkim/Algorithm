import sys
from collections import defaultdict

input = sys.stdin.readline

"""
조건:
  - 중간 결과값은 0~20
  - 마지막 숫자는 결과값
  - 등식이 맞도록 + or - 배치
구현:
  - dfs 나 백트래킹으로 할 경우 2 의 n 승의 시간복잡도 예상
    (물론 중간값 범위가 있어 대부분의 경우의수 패스 할듯)
  - dp 를 통해 해당 차수의 결과값 리스트 관리 ( 최대 스무개임 )
"""

def solution(nums, result):
  N = len(nums)
  dp = [ [0]*21 for _ in range(N) ]
  dp[0][nums[0]] = 1
  for i in range(1, N):
    for j in range(21):
      if dp[i-1][j]:
        if 0<= j-nums[i] <= 20:
          dp[i][j-nums[i]] += dp[i-1][j]
        if 0<= j+nums[i] <= 20:
          dp[i][j+nums[i]] += dp[i-1][j]
  return dp[N-1][result]

# main
N = int(input())
line = list(map(int, input().split()))

print(solution(line[:-1], line[-1]))