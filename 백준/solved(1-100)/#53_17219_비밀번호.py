import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

url_dic={}
for i in range(N):
    line = sys.stdin.readline().strip().split(' ')
    url_dic[line[0]]=line[1]

result = []
for i in range(M):
    url = sys.stdin.readline().strip()
    result.append(url_dic[url])

for r in result:
    print(r)