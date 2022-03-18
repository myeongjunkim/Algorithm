import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
q.append(N)

visited=[-1] * 100001
visited[N] = 0

while q:
    pos = q.popleft()

    if pos == K:
        print(visited[pos])
        break
    else:
        if pos-1 >= 0 and visited[pos-1] ==-1:
            visited[pos-1] = visited[pos]+1
            q.append(pos-1)
        if pos+1 <= 100000 and visited[pos+1] ==-1:
            visited[pos+1] = visited[pos]+1
            q.append(pos+1)
        if pos*2 <=100000 and visited[pos*2]==-1:
            visited[pos*2] = visited[pos]+1
            q.append(pos*2)
