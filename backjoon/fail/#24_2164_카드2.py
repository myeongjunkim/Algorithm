import sys
from collections import deque
N = int(input(''))

q = deque()
q.extend(list(range(1,N+1)))

i = 0
while q:
    num = q.popleft()
    if i%2 != 0:
        q.append(num)
    i +=1

print(num)
