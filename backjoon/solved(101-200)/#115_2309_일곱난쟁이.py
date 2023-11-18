import sys

input = sys.stdin.readline


def solution():

  nums = [ int(input()) for _ in range(9) ]
  
  for i in range(8):
    for j in range(i+1, 9):
      if sum_except_index(nums, i, j) == 100:
        return sorted(get_except_index(nums, i, j))
  return []


def sum_except_index(arr, i, j):
  result = 0
  for iter in range(len(arr)):
    if iter != i and iter != j:
      result += arr[iter]
  return result
  

def get_except_index(arr, i, j):
  result = []
  for iter in range(len(arr)):
    if iter != i and iter != j:
      result.append(arr[iter])
  return result


for nan in solution():
  print(nan)