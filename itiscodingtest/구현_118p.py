"""
게임개발
이것이 코딩테스트다 118p

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

"""


import sys
input = sys.stdin.readline

def get_map(row):
    map = []
    for _ in range(row):
        map.append(list(map(int, input().split())))

    return map

def execute():
    row, col = map(int, input().split())
    x, y, dir = map(int, input().split())
    map_list = []
    for _ in range(row):
        map_list.append(list(map(int, input().split())))
    visit = [[False] * col for _ in range(row) ]
    visit[x][y] = True
    
    # 서 남 동 북
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

  
    cnt = 1

    ing = True
    while ing:
        ending_cnt = 0
        for i in range(dir, dir + 4):
            i %= 4
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= row or ny<0 or ny>= col:
                ending_cnt += 1
                continue

            if map_list[nx][ny] == 0 and visit[nx][ny] is False:
                print(nx, ny)
                x, y = nx, ny
                visit[x][y] = True
                cnt += 1
                dir = i
                break
            else: ending_cnt += 1
            
        if ending_cnt == 4 :
            ing = False

    print(cnt)

execute()