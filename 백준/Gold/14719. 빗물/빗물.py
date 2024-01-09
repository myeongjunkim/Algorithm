import sys

input = sys.stdin.readline

def solution():
  """
  - 블록을 순회하면서 현재 위치에서 왼쪽과 오른쪽의 최대값을 구한다
  - 두 최대값의 최소값을 구한다
  - 구한 최소값에서 현재 높이에서 뺀다
  """
  N, M = map(int, input().split())
  block = list(map(int, input().split()))
  
  result = 0
  for i in range(1, len(block)-1):
    water = min(max(block[:i]), max(block[i+1:])) - block[i]
    if water > 0:
      result += water
    
  print(result)

solution()