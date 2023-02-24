
"""
https://hongcoding.tistory.com/50

d[n][k] n 번째 물건까지 봤을 때 무게가 k 인 배낭의 최대 가치

"""

import sys
input = sys.stdin.readline

def execute():
    N, max_W = map(int, input().split())
    
    bags = [(0,0)]
    for i in range(N):
        bags.append(map(int, input().split()))

    

    dp = [[0]*(max_W+1) for _ in range(N+1)]
   
    for i in range(1, N+1):
        w, v = bags[i]
        for j in range(1, max_W+1):
            if j<w: 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

    print(dp[N][max_W])

execute()