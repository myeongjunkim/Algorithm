import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp_sum = [[0]*(N+1)]
for i in range(1,N+1):
    line = [0] + list(map(int,input().split()))
    dp_line = [0]
    line_sum = 0
    for j in range(1,N+1):
        line_sum += line[j]
        dp_line.append(dp_sum[i-1][j] + line_sum)
    dp_sum.append(dp_line)
    
# print(dp_sum)
result = []
for j in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    r = dp_sum[x2][y2] + dp_sum[x1-1][y1-1]  - dp_sum[x1-1][y2] - dp_sum[x2][y1-1]
    result.append(r)

for _ in result:
    print(_)