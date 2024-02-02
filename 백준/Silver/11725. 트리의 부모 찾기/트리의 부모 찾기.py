import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - N 은 10만
  - 모든 노드의 부모 노드 찾기
  - 루트는 1
구현:
  - 인접노드를 기록한 _map 만들기
  - 루트가 1이므로 1부터 출발
  - 각 노드가 나올 때마다 부모 노드 인덱스 맞춰서 기록
  - 부모노드 순차적으로 출력
"""



def solution(N, connection):
  _map = [[] for i in range(N+1)]
  for a, b in connection:
    _map[a].append(b)
    _map[b].append(a)

  visited = [False]*(N+1)
  result = [0]*(N+1)
  q = deque([1])
  while q:
    pos = q.popleft()
    visited[pos] = True
    for nearby in _map[pos]:
      if visited[nearby]:
        continue
      result[nearby] = pos
      q.append(nearby)
  return result


N = int(input())
connection = [list(map(int, input().split())) for _ in range(N-1)]
result = solution(N, connection)
for i in range(2, N+1):
  print(result[i])

