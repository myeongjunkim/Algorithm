import sys, math

input = sys.stdin.readline

# 3:32

"""
조건:
  - 
구현:
  - 무게중심
"""

def solution(N, _map):

  _map.sort()

  people = sum( p for _, p in _map)
  mid = round(people/2)

  pos_people = 0
  for d, p in _map:
    pos_people += p
    if pos_people >= mid:
      return d
  

  
  
  
# main
N = int(input())
_map = [ list(map(int, input().split())) for _ in range(N) ]
print(solution(N, _map))



