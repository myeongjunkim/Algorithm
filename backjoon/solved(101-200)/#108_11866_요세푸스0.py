import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

num_list = list(range(1,N+1))
res = []

q = deque(num_list)
i = 0
while q:
    i += 1
    n = q.popleft()
    if i != K:
        q.append(n)
    else:
        i=0
        res.append(str(n))
    



print("<"+", ".join(res)+">")