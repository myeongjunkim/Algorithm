import readline
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    tri = [ [0] ]
    for i in range(N):
        tri.append(list(map(int,input().split())))
    if N == 1:
        print(tri[1][0])
    else:
        dp = [ [None], [tri[1][0]], [tri[1][0]+tri[2][0], tri[1][0]+tri[2][1]] ]
        for i in range(3, N+1):
            _new = []
            for j in range(i):
                if j == 0:
                    _new.append(tri[i][j] + dp[i-1][0])
                elif j == i-1:
                    _new.append(tri[i][j] + dp[i-1][i-2])
                else:
                    _new.append(tri[i][j] + max(dp[i-1][j-1], dp[i-1][j]))

            dp.append(_new)
        print(max(dp[N]))

solution()