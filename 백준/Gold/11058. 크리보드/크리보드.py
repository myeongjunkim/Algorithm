import sys

input = sys.stdin.readline

"""
조건:
  - n-1, n-3 항에 의해 n 항이 결정 // N <= 100  -> DP
  - A 출력, 붙여넣기 -> 실질적인 입력
  - 전체 선택, 복사 -> 입력 x
구현:
  - dp
  - n-3 항에서 선택-복사-붙여넣기
"""

def solution(N):
  
  dp = [ 0 for _ in range(N+1) ]
  if N < 7:
    return N
  else: 
    for i in range(N+1):
      dp[i] = i if i < 7 else max( 2*dp[i-3], 3*dp[i-4], 4*dp[i-5] )
        
  return dp[N]

# main
N = int(input())
print(solution(N))