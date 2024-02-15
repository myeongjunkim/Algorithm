"""
dp 개미전사 220p

4
1 3 1 5
-> 8

"""

import sys
input = sys.stdin.readline

def execute():
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [nums[0], max(nums[0], nums[1])]
    for n in range(2, N):
        case1 = dp[n-2] + nums[n]
        case2 = dp[n-1]

        dp.append(max(case1, case2))
    
    print(dp[-1])

execute()
