import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

# 3:32

"""
조건:
  - 강의 시작시간과 종료시간은 10억
  - 강의 개수는 10만
  
구현:
  - 
"""

def solution(N, session):
  heapify(session)
  
  rooms = []
  while session:
    ss = heappop(session)
    if rooms:
      room = heappop(rooms)
      if room > ss[0]:
        heappush(rooms, room)
    heappush(rooms, ss[1])
  
  return len(rooms)

        
  
# main
N = int(input())
session = [ list(map(int, input().split()[1:])) for _ in range(N) ]
print(solution(N, session))


