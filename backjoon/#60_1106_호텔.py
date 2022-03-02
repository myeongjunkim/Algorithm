import sys

def solution():
    C, N = map(int,sys.stdin.readline().strip().split(' '))
    city=[list(map(int, sys.stdin.readline().strip().split(' '))) for i in range(N)]
    city = sorted(city, key= lambda x : x[1])
    dp=[0]
    for c in city:
        c[1]
    print(dp[C])
    
solution()
