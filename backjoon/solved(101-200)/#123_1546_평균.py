import sys

input = sys.stdin.readline


def solution():
  """
  - 최대값 M 을 구한다
  - 값의 합 / M * N * 100
  """
  N = int(input())
  arr = list(map(int, input().split()))

  print( sum(arr)*100 / ( max(arr) * N ) )

solution()