import sys, math

input = sys.stdin.readline

"""
조건:
  - N 은 100만
  - 응시자수 A 는 100만
구현:
  - 
"""

def solution(N, student, B, C):
  result = 0
  for s in student:
    B_cnt = 1
    C_cnt = 0 if (s-B) <= 0 else math.ceil((s-B)/C)
    result += (B_cnt + C_cnt)
  return result


# main

N = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())
print(solution(N, student, B, C))
