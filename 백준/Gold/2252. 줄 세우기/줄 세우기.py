import sys
from collections import deque

input = sys.stdin.readline


"""
조건: 
  - N명 3만, M개의 간선 10만
  
구현:
  - 위상정렬
  - 간선 정보에 해당하는 line_map
  - 들어오는 간선수에 해당하는 line_count
  
"""

def solution(N, lines):
  line_map = [ [] for _ in range(N+1) ]
  line_count = [0] * (N+1)
  for line in lines:
    line_map[line[0]].append(line[1])
    line_count[line[1]] += 1
  
  first_points = [i for i in range(1, N+1) if line_count[i] == 0]
  q = deque(first_points)
  result = []
  while q:
    pos = q.popleft()
    result.append(pos)
    for nearby in line_map[pos]:
      line_count[nearby] -= 1
      if line_count[nearby] == 0:
        q.append(nearby)
  return result
    


# main
N, M = map(int, input().split())
lines = [ list(map(int, input().split())) for _ in range(M) ] 
print(*solution(N, lines))

      