# 다시 볼 문제
# https://zu-techlog.tistory.com/62

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(add, sub, mul, div, result, index):
  global max_val, min_val

  if index == N:
    max_val = max(max_val, result)
    min_val = min(min_val, result)
    return

  if add > 0:
    dfs(add-1, sub, mul, div, result+nums[index], index+1)
  if sub > 0:
    dfs(add, sub-1, mul, div, result-nums[index], index+1)
  if mul > 0:
    dfs(add, sub, mul-1, div, result*nums[index], index+1)
  if div > 0:
    dfs(add, sub, mul, div-1, int(result/nums[index]), index+1)


dfs(add, sub, mul, div, nums[0], 1)

print(max_val)
print(min_val)