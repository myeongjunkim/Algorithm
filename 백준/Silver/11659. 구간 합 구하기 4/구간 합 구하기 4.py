import sys

input = sys.stdin.readline


def solution():
  """
  - 각 인덱스별 누적합을 구한다.
  - 범위가 주어졌을 때 누적합의 차를 통해 구한다.
  """
  N, M = map(int, input().strip().split())  
  arr = list(map(int, input().strip().split()))
  test_case = [ map(int, input().strip().split()) for _ in range(M) ]

  sum_arr = [0]
  temp = 0
  for n in arr:
    temp += n
    sum_arr.append(temp)
  
  for case in test_case:
    start, end = case
    print(sum_arr[end] - sum_arr[start-1])


solution()