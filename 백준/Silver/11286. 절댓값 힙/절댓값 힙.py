import heapq
import sys

input = sys.stdin.readline

def solution():
  N = int(input())
  lines = [ int(input()) for _ in range(N) ]

  heap = []
  for line in lines:
    if line == 0:
      if heap  == []:
        print(0)
      else:
        pos = heapq.heappop(heap)
        print(pos[1])
    else:
      heapq.heappush(heap, (abs(line), line))
  


solution()