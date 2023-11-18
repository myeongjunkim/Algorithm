import sys
from collections import deque
N = int(input(''))
map = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(N)]

def is_paper(map, r,c, N):
    result = True
    point = map[r][c]
    for i in range(r,r+N):
        for j in range(c, c+N):
            if point != map[i][j]:
                result = False
                break
        if result == False:
            break
    return result

def get_split_point(r, c, N):
    points=[]
    for i in range(r,r+N,N//3):
        for j in range(c,c+N,N//3):
            points.append([i,j])
    return points


result_dic = {-1:0, 0:0, 1:0}
queue = deque()
r, c = 0, 0

if is_paper(map, r,c, N):
    result_dic[map[r][c]] += 1
else:
    queue.append(get_split_point(r, c, N))
    while queue:
        points = queue.popleft()
        N = points[1][1] - points[0][1]
        for point in points:
            r, c = point[0], point[1]
            if is_paper(map, r,c, N):
                result_dic[map[r][c]] += 1
            elif N == 3:
                for i in range(r,r+N):
                    for j in range(c,c+N):
                        result_dic[map[i][j]] += 1
            else:
                queue.append(get_split_point(r, c, N))
        

print(result_dic[-1])
print(result_dic[0])
print(result_dic[1])