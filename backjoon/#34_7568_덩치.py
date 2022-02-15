import sys

T = int(input(''))

person_data = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(T)]

# data_sorted = sorted(person_data, key= lambda x : (x[0], x[1]))
# print(data_sorted)

for p in person_data:
    cnt = 1
    for all in person_data:
        if p[0]< all[0] and p[1]< all[1]:
            cnt +=1
    print(cnt)