import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    home_pay = [None]
    for i in range(N):
        home_pay.append(list(map(int, input().split(' '))))
    dp=[ [0,0,0], home_pay[1] ]
    for i in range(2, N+1):
        case_0 = min(dp[i-1][1], dp[i-1][2]) + home_pay[i][0]
        case_1 = min(dp[i-1][0], dp[i-1][2]) + home_pay[i][1]
        case_2 = min(dp[i-1][0], dp[i-1][1]) + home_pay[i][2]
        dp.append([case_0, case_1, case_2])
    print(min(dp[N]))

solution()