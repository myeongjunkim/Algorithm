import sys
input = sys.stdin.readline


pok_int_name = {}
pok_name_int = {}
N, M = map(int, input().split())
for i in range(1,N+1):
    name = input()[:-1]
    pok_int_name[i] = name
    pok_name_int[name] = i

res = []
for i in range(M):
    line = input()[:-1]
    print(line)
    if line.isdigit():
        res.append(pok_int_name[int(line)])
    else:
        res.append(pok_name_int[line])


for r in res:
    print(r)

