import sys

input = sys.stdin.readline


def solution():

  N, M = map(int, input().split())
  
  n = 1
  cnt = 0
  num_list = []
  for _ in range(M):
    num_list.append(n)
    cnt += 1
    if cnt >= n:
      n += 1
      cnt = 0
    
  print(sum(num_list[N-1:M]))
    

solution()