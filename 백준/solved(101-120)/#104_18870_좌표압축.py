import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


res = [None]*N

num_list = []
for i in range(N):
    num_list.append((nums[i], i))

num_list.sort()

index = 0
pos = num_list[0][0]
for n, i in num_list:
    if pos < n:
        index +=1
    res[i] = index
    pos = n

for i in range(N):
    if i == N-1:
        print(res[i])
    else:
        print(res[i], end=" ")