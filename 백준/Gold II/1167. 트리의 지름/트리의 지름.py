import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건:
  - 
구현:
  - dfs 를 통해 모든 노드에 양쪽의 각 최대거리 값을 기록
  - 모든 노드 돌면서 양쪽거리합의 최대값 구하기
"""

def solution(N, lines):
  
  node_dist = [ [] for _ in range(N+1)]
  visited = [False]*(N+1)
  def dfs_for_dist(pre_n, pos_w, pos_n):
    nonlocal lines, node_dist, visited
    visited[pos_n] = True
    for next_w, next_n in lines[pos_n]:
      if visited[next_n]:
        continue
      visited[next_n] = True
      dfs_for_dist(pos_n, next_w, next_n)

    pos_max_dist = max(node_dist[pos_n]) if node_dist[pos_n] else 0
    node_dist[pre_n].append( pos_max_dist + pos_w )

  dfs_for_dist(0, 0, 1)
  max_d = 0
  for dists in node_dist:
    if len(dists) > 2:
      dists = sorted(dists)
      d = dists.pop() + dists.pop()
    else:
      d = sum(dists)
    max_d = max(max_d, d)
  return max_d

# main
N = int(input())
lines = [ [] for _ in range(N+1)]
for _ in range(N):
  line = list(map(int, input().split()))
  line = line[::-1]
  a = line.pop()
  while line[-1] != -1:
    b, w = line.pop(), line.pop()
    lines[a].append((w,b))
print(solution(N, lines))
