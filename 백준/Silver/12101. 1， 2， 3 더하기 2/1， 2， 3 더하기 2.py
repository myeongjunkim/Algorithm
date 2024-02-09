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


def solution(N, K):

  dp = [ [] for _ in range(N+4) ]
  dp[1].extend(["1"])
  dp[2].extend(["11", "2"])
  dp[3].extend(["111", "12", "21", "3"])

  if N > 3:
    for i in range(4, N+1):
      for case_str in dp[i-1]:
        dp[i].append(case_str+"1")
      for case_str in dp[i-2]:
        dp[i].append(case_str+"2")
      for case_str in dp[i-3]:
        dp[i].append(case_str+"3")

  if len(dp[N]) < K:
    return "-1"
  return "+".join(list(sorted(dp[N])[K-1]))
  
# main
N, K = map(int, input().split())
print(solution(N, K))

