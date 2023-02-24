"""
dp 바닥공사 223p

1x2 2x1 2x2

2xn 방법수

3 -> 5

"""

import sys
input = sys.stdin.readline

def execute():
    N = int(input())
    
    dp = [None] *1001
    dp[1] = 1
    dp[2] = 3
    for n in range(3,N+1):
        case1 = dp[n-1]
        case2 = dp[n-2]*2
        dp[n] = case1+case2

    print(dp[N])

execute()


