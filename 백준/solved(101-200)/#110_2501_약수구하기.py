from sys import stdin

input = stdin.readline


def solution():

  N, K = map(int, input().split())
  count = 0
  for i in range(1,N+1):
    if N%i == 0:
      count += 1
    if count == K:
      return i

  return 0

print(solution())