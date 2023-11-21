import sys

input = sys.stdin.readline


def solution():

  M = int(input())
  N = int(input())

  num_list = []
  for i in range(M, N+1):
    if is_real(i):
      num_list.append(i)

  if num_list != []:
    print(sum(num_list))
    print(num_list[0])
  else:
    print(-1)


def is_real(n):
  if n == 1:
    return False
  flag = True
  for i in range(2, n):
    if n % i == 0:
      flag = False
      break
  return flag

solution()