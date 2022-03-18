import sys
from collections import deque
input = sys.stdin.readline

from queue import PriorityQueue

N, K = map(int, input().split())

# que = PriorityQueue()
# que.put((1,N))


q = deque()
q.append(N)

visited=[-1] * 100001
visited[N] = 0

while q:
    pos = q.popleft()
    # pos = que.get()[1]
    if pos == K:
        print(visited[pos])
        break
    else:
        if pos*2 <=100000 and visited[pos*2]==-1:
            visited[pos*2] = visited[pos]
            # que.put((1,pos*2))
            q.appendleft(pos*2)

        if pos-1 >= 0 and visited[pos-1] ==-1:
            visited[pos-1] = visited[pos]+1
            # que.put((2,pos-1))
            q.append(pos-1)

        if pos+1 <= 100000 and visited[pos+1] ==-1:
            visited[pos+1] = visited[pos]+1
            # que.put((2,pos+1))
            q.append(pos+1)
