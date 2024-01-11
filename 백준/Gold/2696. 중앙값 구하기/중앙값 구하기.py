import heapq
from collections import deque
import sys

input = sys.stdin.readline

"""
조건: 
  - 테스트케이스 1000개
  - 수열의 크기 10000개 ( n 은 1만 임을 고려 )
구현:
  - 최소힙에 배열 저장
  - pop 하면서 리스트에 저장
  - 홀수 값일 때 k//2 인덱스의 원소 가 중앙값임을 활용
"""

def solution():
  N = int(input())
  test_case = []
  for _ in range(N):
    M = int(input())
    line = []
    for _ in range(M//10):
      line.extend( list(map(int, input().split())) )
    if M%10 != 0:
      line.extend( list(map(int, input().split())) )
    test_case.append(line)

  result_case = []
  for case in test_case:
    result = []
    heap = []
    heapq.heapify(heap)
    for i in range(len(case)):
      heapq.heappush(heap, case[i])
      
      if i % 2 == 0:
        get_list = []
        for _ in range(i//2 + 1):
          n = heapq.heappop(heap)
          get_list.append(n)
        result.append(get_list[-1])
        while get_list:
          heapq.heappush(heap, get_list.pop())
          
    result_case.append(result)


  for res in result_case:
    count = len(res)
    line = []
    print(count)
    for i, val in enumerate(res):
      if i % 10 == 9 or i == count-1:
        print(val, end="\n")
      else:
        print(val, end=" ")
    
      
solution()