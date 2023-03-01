# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python

import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N ,K = map(int, input().strip().split())


dia_list = []
for _ in range(N):
    m, v = map(int, input().strip().split())
    heappush(dia_list, (m, v))

bag_list = []
for _ in range(K):
    bag = int(input().strip())
    heappush(bag_list, bag)


res = 0
temp_dia_list = []
while bag_list:
    bag = heappop(bag_list)
    while dia_list and dia_list[0][0] <= bag:
        heappush(temp_dia_list, -heappop(dia_list)[1])
    if temp_dia_list:
        res -= heappop(temp_dia_list)
    
print(res)