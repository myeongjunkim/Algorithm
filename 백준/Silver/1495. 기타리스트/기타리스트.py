import sys

input = sys.stdin.readline

"""
조건: 
  - 곡의 길이 N 50
  - 최대 볼륨 M 1000
  - 0~M 사이 볼륨
  - i번 곡은 P+V[i]나 P-V[i] 로 연주
  
구현:
  - dp 의 각 인덱스에 가능한 경우 모두 저장
  - 마지막 인덱스에서 리스트의 최대값

  - dfs 를 통해 depth 가 N 인 것까지 조사
  - depth 가 N 일 때 max 값 update
  

"""



def solution(N, S, M, V):

  def dp():
    dp =  [ [False]*(M+1) for _ in range(N) ]

    pre_result = [False]*(M+1)
    pre_result[S] =True
    for i in range(N):
      for j in range(M+1):
        if not pre_result[j]:
          continue
        if 0<=j+V[i]<=M:
          dp[i][j+V[i]] = True
        if 0<=j-V[i]<=M:
          dp[i][j-V[i]] = True
      pre_result = dp[i]
      
    return dp

  result = dp()
  for i in range(M, -1, -1):
    if result[-1][i]:
      return i
  return -1

  # max_vol = -1
  # def dfs(pos, depth):
  #   nonlocal max_vol
  #   if depth == N:
  #     max_vol = max(max_vol, pos)
  #     return

  #   if 0<=pos+V_list[depth]<=M:
  #     dfs(pos+V_list[depth], depth+1)
  #   if 0<=pos-V_list[depth]<=M:
  #     dfs(pos-V_list[depth], depth+1)

  # dfs(S, 0)
  # return max_vol
  

# main
N, S, M = map(int, input().split())
V_list = list(map(int, input().split()))
print(solution(N, S, M, V_list))


