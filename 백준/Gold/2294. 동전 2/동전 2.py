import sys

input = sys.stdin.readline

"""
조건: 
  - N 종류의 동전
  - k 의 가치
구현:
  - dp 는 i번째에 i원의 가치를 만드는 동전의 최소개수를 저장
  - i번째 원소의 값 구하기
    min(dp[i-coin1],,,)
"""


def solution(k, coins):
  
  dp =[0]*(k+1)

  for i in range(1, k+1):
    min_list = []
    for c in coins:
      if i-c == 0:
        min_list.append(1)
      elif i-c > 0 and dp[i-c] > 0:
        min_list.append(dp[i-c]+1)
    dp[i] = min(min_list) if min_list else 0
  
  return dp[k] if dp[k] != 0 else -1
    
    

# main
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
print(solution(k, coins))

      