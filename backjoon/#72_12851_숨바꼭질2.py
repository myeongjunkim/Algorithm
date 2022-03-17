import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().split())

visited=[-1]*200001
visited[N] = 1
queue = deque()
queue.append(N)
while queue:
    pos = queue.popleft()

    if pos == K:
        print(visited[pos]+1)
        print(visited.count(visited[pos]+1))
        break

    if visited[pos-1] == -1 and pos-1 >= 0:
        queue.append(pos-1)
        visited[pos-1] = visited[pos] + 1
    
    if visited[pos+1] == -1 and pos+1 <= 100000:
        queue.append(pos+1)
        visited[pos+1] = visited[pos] + 1

    if visited[2*pos] == -1 and 2*pos <= 200000:
        queue.append(pos*2)
        visited[pos*2] = visited[pos]
    
