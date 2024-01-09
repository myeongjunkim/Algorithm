import sys
input = sys.stdin.readline

N = int(input())

res = []
for i in range(N):
    n, name = input().split()
    n = int(n)
    res.append((n,i, name))

res = sorted(res, key=lambda x: (x[0], x[1]))
for r in res:
    print(f"{r[0]} {r[2]}")