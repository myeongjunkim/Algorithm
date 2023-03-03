
"""
다이나믹 프로그래밍 217p
5로 나누기, 3으로 나누기, 2로 나누기, 1 빼기
1로 만들기

"""


# 이전 단계가 무엇이었는지 저장.

import sys
input = sys.stdin.readline

def solution(X):
    dp = [None, 0, 1]
    for n in range(3, X+1):
        find_dp = [dp[n-1]]
        if n%5 == 0:
            find_dp.append(dp[n//5])
        if n%3 == 0:
            find_dp.append(dp[n//3])
        if n%2 == 0:
            find_dp.append(dp[n//2])
        dp.append(min(find_dp)+1)

    return dp[X]

X = int(input())
print(solution(X))


