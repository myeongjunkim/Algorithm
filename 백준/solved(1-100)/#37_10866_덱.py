from collections import deque
import sys

T = int(input(''))

commends = [sys.stdin.readline().strip().split(' ') for i in range(T)]

queue = deque()
for commend in commends:
    if commend[0] == 'push_front':
       num = int(commend[1])
       queue.appendleft(num)
    elif commend[0] == 'push_back':
       num = int(commend[1])
       queue.append(num)
    elif commend[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commend[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)    
    elif commend[0] == 'size':
        print(len(queue))
    elif commend[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif commend[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    