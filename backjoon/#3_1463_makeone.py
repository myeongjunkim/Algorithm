def solution(N):
    dp = [0,0]
    for i in range(2,N+1):
        temp=[]
        if i%3 == 0:
            temp.append(dp[i//3])
        if i%2 == 0:
            temp.append(dp[i//2])
        temp.append(dp[i-1])
        dp.append(min(temp)+1)
    return dp[N]


N = int(input())
print(solution(N))