"""
dp 효율적인 화폐 구성 226p

N 가지 화폐로 M 만들기

2 15
2
3
->5

3 4
3
5
7
-> -1

"""

import sys
input = sys.stdin.readline

def execute():
    N, M = map(int, input().split())
    nums = []
    for i in range(N):
        nums.append(int(input()))
    # nums.sort()

    dp = [-1]*10001 
    dp[0] = 0

    for won in range(M+1):
        
        
        case_list = []
        for n in nums:
            if won-n >= 0 and dp[won-n] != -1:
                case_list.append(dp[won-n]+1)

        if case_list != []:
            dp[won] = min(case_list)
        
        
    print(dp[:M+1])
    if dp[M]: print(dp[M])
    else: print(-1)

execute()

