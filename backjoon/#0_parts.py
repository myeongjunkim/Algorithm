import sys
num=sys.stdin.readlines()

import sys
T = int(input(''))

num_list = [int(sys.stdin.readline().strip()) for i in range(T)]

points = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(T)]



from collections import deque
queue = deque([4, 5, 6])
queue.append(7)
deque([4, 5, 6, 7])
queue.popleft()

# 람다 정렬
points= sorted(points, key = lambda x : (x[1],x[0]))