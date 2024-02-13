import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

"""
조건:
  - N 은 1-14

구현:
  - 백트래킹. 
  - 모든 격자를 순회하면서 
"""

def solution(N):
  queen = [0] * N
  result = 0

  def is_possible(queen, r):
    for i in range(r):
      if queen[r] == queen[i] or abs(queen[r] - queen[i]) == abs(r-i):
        return False
    return True


  def back_tracking(r):
    nonlocal N, result, queen
    if r == N:
      result += 1
      return

    for c in range(N):
      queen[r] = c
      if is_possible(queen, r):
          back_tracking(r+1)

  back_tracking(0)
  return result


# main
N = int(input())
print(solution(N))
