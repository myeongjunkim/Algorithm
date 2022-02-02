import math

def get_case(data):
    x1, y1 = data[0], data[1]
    x2, y2 = data[3], data[4]
    r1, r2 = data[2], data[5]

    if x1 == x2 and y1==y2 and r1 == r2:
        return -1
            
    r_min = min(r1, r2)
    r_max = max(r1, r2)
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if r_min + d > r_max:
        if (r_max + r_min) > d:
            return 2
        elif (r_max + r_min) == d:
            return 1
        else:
            return 0
    elif r_min + d == r_max:
        return 1
    else:
        return 0


N = int(input(''))

data_set=[]
for i in range(N):
    data = list(map(int, input('').split(' ')))
    data_set.append(data)

result = []
for data in data_set:
    result.append(get_case(data))

for r in result:
    print(r)