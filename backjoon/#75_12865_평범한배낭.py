import sys
input = sys.stdin.readline

N ,K = map(int,input().split())

items = []
for i in range(N):
    items.append(list(map(int,input().split())))

items.sort()

print(items)


# 1키로일때, ,,, N키로일때
