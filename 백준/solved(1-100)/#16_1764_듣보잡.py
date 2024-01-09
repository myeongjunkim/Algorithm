import sys
input = sys.stdin.readline

N, M  = map(int,input().strip().split())

hash = {}
for i in range(N):
    hash[input().strip()] = 0



res=[]
for i in range(M):
    line = input().strip()
    try:
        hash[line]
        res.append(line)
    except:
        pass


res.sort()
print(len(res))
for r in res:
    print(r)

