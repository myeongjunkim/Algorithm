import sys
input = sys.stdin.readline

def get_dp(numlist):
    if len(numlist) == 1:
        return max(numlist[0])

    dp = [ [numlist[0][0], numlist[0][1]], 
            [numlist[0][1]+numlist[1][0], numlist[0][0]+numlist[1][1]] 
        ]
    for i in range(2, len(numlist)):
        dp.append([
            max(dp[i-1][1], dp[i-2][1]) + numlist[i][0],
            max(dp[i-1][0], dp[i-2][0]) + numlist[i][1],
        ])

    return max(dp[-1])

T = int(input())
result = []
for i in range(T):
    n = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    numlist=[]
    for j in range(n):
        numlist.append([line1[j], line2[j]])

    result.append(get_dp(numlist))

for _ in result:
    print(_)