import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))


# 10, 20, 1,2,3,4,5,6,7,8,9, 30, 40 

dp=[1 for i in range(N)]
min_n = num_list[0]
for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 거의 배낀듯,,, 방법을 배우자,,,