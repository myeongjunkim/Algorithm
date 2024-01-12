import sys
import heapq

input = sys.stdin.readline

"""
조건: 
  - N 종류의 동전
  - k 의 가치
구현:
  - 0부터 k 까지 순차적으로 경우의수 조사
  - 이전 단계들의 합으로 현재 단계의 경우의수 구하기 ( dp, 점화식 )
마무리: 
  - i 를 먼저 돌 경우 겹치는 것을 체크하지 못함
  - coin 을 먼저도는 방식을 통해 겹치지 않도록
"""


def solution():
  n, k = map(int, input().split())
  coins = [int(input()) for _ in range(n)]
  coins = sorted(coins)

  dp = [0]*(k+1)
  dp[0] = 1
  for coin in coins:
    for i in range(coin, k+1):
      dp[i] += dp[i-coin]
  print(dp[k])
  

solution()

      