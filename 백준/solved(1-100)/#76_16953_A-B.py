import sys
from collections import deque

input=sys.stdin.readline

# main
def sol(A, B):
    q = deque()
    q.append([A,1])

    while q:
        num, cnt = q.popleft()
        if num == B:
            return cnt

        if num*2 <= B:
            q.append([num*2, cnt + 1])

        if num*10+1 <= B:
            q.append([num*10+1, cnt+1])

    return -1



A, B = map(int, input().split())
print(sol(A, B))