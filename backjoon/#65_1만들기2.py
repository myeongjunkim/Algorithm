import sys
input = sys.stdin.readline

[최소 회수, 전 단계 인덱스(i)]

def solution():
    N = int(input())
    dp = [[0, 0], [0, 0], [1, 1]]
    for i in range(3, N+1):
        temp=[]
        if i%3 == 0:
            temp.append([dp[i//3][0]+1, i//3])
        if i%2 == 0:
            temp.append([dp[i//2][0]+1, i//2])
        temp.append([dp[i-1][0]+1, i-1])
        temp.sort()
        dp.append(temp[0])
    print(dp[N])