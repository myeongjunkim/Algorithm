import sys
from collections import deque

def get_split(N, point):
    splited_points = [
            [point[0]+N//2, point[1]+N//2, N//2],
            [point[0]+N//2, point[1], N//2],
            [point[0], point[1]+N//2, N//2],
            [point[0], point[1], N//2]
        ]
    return splited_points


def check_one(point, map):
    r, c, N = point[0], point[1], point[2]
    standard = map[r][c]
    flag = True
    for i in range(N):
        for j in range(N):
            if map[r+i][c+j] != standard:
                flag = False
                break
    if flag:
        return str(standard)
    else:
        return "again"



N = int(input(''))
map = []
for i in range(N):
    line = sys.stdin.readline().strip()
    line_list = []
    for n in line:
        line_list.append(int(n))
    map.append(line_list)


# main
result=""
stack =[]
stack.append([0,0,N])
while len(stack) !=0:
    point = stack.pop()
    if point == ")":
        result += point
    else:
        N = point[2]
        if check_one(point,map) == "again":
            result += "("
            stack.append(")")
            stack.extend(get_split(N, point))
        else:
            result += check_one(point, map)
    


print(result)