import sys
from collections import deque

N ,K = map(int, sys.stdin.readline().strip().split(' '))

dia_list = [[list(map(int, sys.stdin.readline().strip().split(' '))),1] for i in range(N)]
bag_list = [int(sys.stdin.readline().strip()) for i in range(K)]

dia_list = sorted(dia_list, key= lambda x:x[1])

sum = 0
for bag_size in bag_list:
    for dia in dia_list:
        if dia[1] and bag_size >= dia[0][0]:
            sum += dia[0][1]
            dia[1] = 0
            break


print(sum)


