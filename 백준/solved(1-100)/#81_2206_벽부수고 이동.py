import sys
from collections import deque
input= sys.stdin.readline

N, M = map(int, input().strip().split())

map_list=[]
for i in range(N):
    line = input().strip()
    line_list=[]
    for c in line:
        line_list.append(int(c))
    map_list.append(line_list)

visited = [[[0, 0] for j in range(M)] for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# data = [pos, is_one, cnt]


def bfs():
    q = deque()
    q.append([[0,0], 0])
    visited[0][0][0] = 1
    while q:
        data = q.popleft()
        pos, iscrash = data[0], data[1]
        r, c = pos[0], pos[1]
        # print(cnt, pos)

        if r == N-1 and c == M-1:
            return visited[r][c][iscrash]

        for i in range(4):
            new_r = r + dx[i]
            new_c = c + dy[i]

            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
                continue

            if map_list[new_r][new_c] == 0 and visited[new_r][new_c][iscrash] == 0:
                q.append([[new_r, new_c], iscrash])
                visited[new_r][new_c][iscrash] = visited[r][c][iscrash] + 1

            if map_list[new_r][new_c] == 1 and iscrash == 0:
                q.append([[new_r, new_c], iscrash+1])
                visited[new_r][new_c][iscrash+1] = visited[r][c][iscrash] + 1
                

    return -1

print(bfs())

# 못해먹겠다,, 어려워,,, 시작이반 블로그 참고