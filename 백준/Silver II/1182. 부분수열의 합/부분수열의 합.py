import sys
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건:
  - N 은 20, S 는 백만
  - 각 원소의 절대값은 10만
구현:
  - 백트래킹 or 완전탐색
  - 1부터 N 까지 
"""

def solution(N, S, nums):
  count = 0
  visited = [False] * N
  def dfs(pos, result, depth):
    nonlocal S, nums, count
    if result == S and depth != 0:
      count += 1
    
    for i in range(pos, N):
      if visited[i]:
        continue
      visited[i] = True
      dfs(i, result+nums[i], depth+1)
      visited[i] = False
  dfs(0,0,0)
  return count
  

# main
N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, S, nums))
