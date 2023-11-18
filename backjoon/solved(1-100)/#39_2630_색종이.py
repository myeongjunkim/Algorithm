import sys
from collections import deque

def check_paper(point, map):
    r, c, N = point[0], point[1], point[2]
    flag =True
    for i in range(N):
        if flag == False:
            break
        for j in range(N):
            if map[r][c] != map[r+i][c+j]:
                flag=False
                break
    if flag:
        return map[r][c]
    else:
        return "again"


def split_paper(point):
    N = point[2]
    splited_points=[
        [point[0], point[1], N//2],
        [point[0], point[1]+N//2, N//2],
        [point[0]+N//2, point[1], N//2],
        [point[0]+N//2, point[1]+N//2, N//2]
    ]
    return splited_points


N = int(input(''))
map = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(N)]
    

cnt_0, cnt_1 = 0, 0

queue = deque()
queue.append([[0,0, N]])
while queue:
    points = queue.popleft()
    for point in points:
        result = check_paper(point, map)
        if result == "again":
            queue.append(split_paper(point))
        elif result ==1:
            cnt_1 +=1
        elif result == 0:
            cnt_0 += 1




print(cnt_0)
print(cnt_1)
