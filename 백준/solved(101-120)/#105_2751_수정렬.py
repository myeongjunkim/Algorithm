import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N = int(input())
heap = []
for i in range(N):
    heappush(heap, int(input()))

for i in range(N):
    print(heappop(heap))
