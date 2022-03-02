import sys
input=sys.stdin.readline

N = int(input())
step=[0]
step.extend([int(input()) for i in range(N)])

if N == 1:
    print(step[1])
else:
    dp = [[0,0], [step[1], step[1]], [step[1]+step[2], step[2]]]
    for i in range(3, N+1):
        dp.append([dp[i-1][1] + step[i], max(dp[i-2]) + step[i]]) 
    
    print(max(dp[N]))


