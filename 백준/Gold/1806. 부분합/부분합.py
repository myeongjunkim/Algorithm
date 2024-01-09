import sys

input = sys.stdin.readline


def solution():
  """
  - arr 순회하여 누적합 arr_sum 구하기
  - arr_sum 에 두개의 포인터 start, end
  
  - end 가 target 값 도달할 때까지 +1 하며 start, end 차 구하기
  - target 값 넘어가면 start +1 하며 start, end 차 구하기
  - min(end-start, result)
  """
  N, S = map(int, input().split())
  arr = list(map(int, input().split()))
  arr_sum = cal_arr_sum(arr)

  start =  0
  min_len = N+1
  for end in range(0,N+1):
    while arr_sum[end] - arr_sum[start] >= S and start < end:
      min_len = min(end-start, min_len)
      start += 1

  if min_len == N+1:
    print(0)
  else:
    print(min_len)
    
  

def cal_arr_sum(arr):
  result = [0]
  pos = 0
  for n in arr:
    pos += n
    result.append(pos)
  return result
  
solution()

