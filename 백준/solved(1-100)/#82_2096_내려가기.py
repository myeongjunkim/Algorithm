import sys
input = sys.stdin.readline

N = int(input())

first_line = list(map(int,input().split()))

dp_max_temp = first_line
dp_min_temp = first_line

dp_max = [max(dp_max_temp)]
dp_min = [min(dp_min_temp)]

for i in range(1, N):
    line = list(map(int,input().split()))
    max_0 = max(dp_max_temp[0], dp_max_temp[1]) + line[0]
    max_1 = max(dp_max_temp[0], dp_max_temp[1], dp_max_temp[2]) + line[1]
    max_2 = max(dp_max_temp[1], dp_max_temp[2]) + line[2]
    dp_max_temp = [max_0, max_1, max_2]
    dp_max.append(max(dp_max_temp))

    min_0 = min(dp_min_temp[0], dp_min_temp[1]) + line[0]
    min_1 = min(dp_min_temp[0], dp_min_temp[1], dp_min_temp[2]) + line[1]
    min_2 = min(dp_min_temp[1], dp_min_temp[2]) + line[2]
    dp_min_temp = [min_0, min_1, min_2]
    dp_min.append(min(dp_min_temp))



print(dp_max[N-1], dp_min[N-1])