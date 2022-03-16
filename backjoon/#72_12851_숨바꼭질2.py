import sys
from collections import deque

input = sys.stdin.readline

def get_gap(a,b):
    result = a-b
    if result<0:
        return -result
    return result

def get_case(num, K):
    nearby=[]
    if visited[num-1] == False and num != 0:
        nearby.append(num-1)
    if visited[num+1] == False and num < K:
        nearby.append(num+1)
    if visited[num*2] == False :
        if get_gap(num, K) > get_gap(num*2, K):
            nearby.append(num*2)

    return nearby


N, K = map(int, input().split())

visited=[False]*200001
visited[N] = True
queue = deque()
queue.append(get_case(N, K))
cnt = 1
while queue:
    nearby = queue.popleft()
    # print(nearby)
    new_nearby = []
    case_cnt = 0
    for p in nearby:
        if p == K:
            case_cnt +=1
        else:
            visited[p] = True
            new_nearby.extend(get_case(p, K))
    if case_cnt:
        break
    queue.append(new_nearby)
    cnt +=1

print(cnt)
print(case_cnt)