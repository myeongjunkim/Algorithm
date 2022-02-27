from hashlib import new
import sys

N = int(input(''))

time_list = []
for i in range(N):
    time_list.append(list(map(int, sys.stdin.readline().strip().split(' '))))

time_list = sorted(time_list, key= lambda x: (-x[1], -x[0]))

# print(time_list)

result = [time_list.pop()]
while time_list:
    new_part_time = time_list.pop()
    if new_part_time[0] >= result[-1][1]:
        result.append(new_part_time)


print(len(result))