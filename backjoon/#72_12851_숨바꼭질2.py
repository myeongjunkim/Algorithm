import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().split())

visited=[-1]*100001
visited[N] = 0
queue = deque()
queue.append([N,0])
countdic = {}
while queue:
    pos, length = queue.popleft()
    # print(pos, visited[pos], result,flag)
    visited[pos] = 0 

    if pos == K:
        try:
            countdic[length] +=1
        except KeyError:
            countdic[length] = 1

    
    else:
        if pos-1 >= 0 and visited[pos-1] == -1 :
            queue.append([pos-1, length+1])
        
        if pos+1 <= 100000 and visited[pos+1] == -1 :
            queue.append([pos+1, length+1])

        if 2*pos <= 100000 and visited[2*pos] == -1:
            queue.append([pos*2, length+1])



key = list(countdic.keys())[0]
print(key)
print(countdic[key])