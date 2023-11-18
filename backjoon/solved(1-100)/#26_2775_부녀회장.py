import sys
input = sys.stdin.readline

T = int(input())

case_list = []
for i in range(T):
    case = []
    for j in range(2):
        case.append(int(input()))
    case_list.append(case)

sorted_case_list = sorted(case_list, reverse=True)


# case = [층, 호]

dp = [list(range(15))]

for i in range(1,sorted_case_list[0][0]+1):
    new_dp = [0]
    for j in range(1, 15):
        new_dp.append(sum(dp[i-1][:j+1]))
    dp.append(new_dp)


for case in case_list:
    print(dp[case[0]][case[1]])