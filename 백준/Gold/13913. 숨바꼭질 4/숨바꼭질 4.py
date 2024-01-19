import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - N, K 는 10만
  - K 는 목표값
  - N -> X-1 or X+1 or 2*X
  - 
  
구현:
  - bfs 를 통해 탐색, 인접한 그래프는 N 이 갈 수 있는 정점 세가지
    - K 보다 커지는 경우는 K - pos 를 통해 바로 해 구하기
  - 인접한 그래프가 이미 방문한 노드라면 포함 X
  - 노드에 path 포함

  -> path+[node] 식으로 path 를 기록하게 될 경우 path 선언과정에서 O(n) 만큼 발생
  -> rout 리스트를 만들고 이전 노드를 기록하는 식으로 해야함
"""

def solution(N, K):
  global pre_node
  if N > K:
    for i in range(K, N):
      pre_node[i] = i+1
    return N - K

  dist = [0] * 100_001
  
  q = deque([N])
  while q:
    pos = q.popleft()
    if pos == K:
      return dist[pos]

    for next_pos in [pos-1, pos+1, pos*2]:
      if next_pos <= 100_000 and next_pos >= 0 and not dist[next_pos]:
        q.append(next_pos)
        dist[next_pos] = dist[pos] + 1
        pre_node[next_pos] = pos
    
  return 0
      

# main
N, K = map(int, input().split())
pre_node = [-1] * 100_001

result = solution(N, K)
route, pos = [K], K
for _ in range(result):
  pos = pre_node[pos]
  route.append(pos)
  
print(result)
print(*route[::-1])
