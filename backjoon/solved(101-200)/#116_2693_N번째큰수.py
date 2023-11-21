import sys

input = sys.stdin.readline


def solution():
  N = int(input())
  test_case = [ list(map(int, input().split())) for _ in range(N) ]

  for case in test_case:
    sorted_case = sorted(case)
    print(sorted_case[-3])


solution()