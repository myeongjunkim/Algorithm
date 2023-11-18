import sys

input = sys.stdin.readline



def solution():
  N = int(input())
  nums = list(map(int, input().split()))

  min_int = 1_000_000
  max_int = -1_000_000

  for n in nums:
    if n > max_int:
      max_int = n
    if n < min_int:
      min_int = n

  print(min_int, max_int)


solution()