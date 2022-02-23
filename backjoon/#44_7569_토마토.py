import sys
from collections import deque

def get_nearby(point, box):
    H, R, C= len(box)-1, len(box[0])-1, len(box[0][0])-1
    h, r, c = point[0], point[1], point[2]
    nearby = []
    if h !=0 and box[h-1][r][c] == 0:
        nearby.append([h-1, r, c])
        box[h-1][r][c] = 1
    if h != H and box[h+1][r][c] == 0:
        nearby.append([h+1, r, c])
        box[h+1][r][c] = 1
    if r !=0 and box[h][r-1][c] == 0:
        nearby.append([h, r-1, c])
        box[h][r-1][c] = 1
    if r != R and box[h][r+1][c] == 0:
        nearby.append([h, r+1, c])
        box[h][r+1][c] = 1
    if c !=0 and box[h][r][c-1] == 0:
        nearby.append([h, r, c-1])
        box[h][r][c-1] = 1
    if c != C and box[h][r][c+1] == 0:
        nearby.append([h, r, c+1])
        box[h][r][c+1] = 1

    return nearby


def check_completed(box):
    H, R, C= len(box), len(box[0]), len(box[0][0])
    flag = True
    for h in range(H):
        if flag:
            for r in range(R):
                if 0 in box[h][r]:
                    flag=False
                    break
        else:
            break
    return flag


C, R, H = map(int,input('').split(" "))
box = []
for h in range(H):
    box.append([list(map(int,sys.stdin.readline().strip().split(' '))) for r in range(R)])


# 1인 애들, -1 인 애들 인덱스 다 수집해! => 몇층 몇바이 몇
# 1인 애들 큐에 넣어놓기

# 인접 토마토 인덱스 get하는 함수 하나 만들기(-1위치는 거르고, 0인 애들 인덱스만)

# 이거 다 큐에 넣고 하나씩 빼서 반복

# day카운트가 변화하지 않으면 종료


one_index=[]
minus_index=[]

for h in range(H):
    for r in range(R):
        for c in range(C):
            if box[h][r][c] == 1:
                one_index.append([h,r,c])
            elif box[h][r][c] == -1:
                minus_index.append([h,r,c])

queue = deque()
queue.append(one_index)

day = 0
while queue:
    get_one = queue.popleft()
    new_one=[]
    for index in get_one:
        new_one.extend(get_nearby(index, box))
    if new_one:
        queue.append(new_one)
        day +=1


if check_completed(box):
    print(day)
else:
    print(-1)
