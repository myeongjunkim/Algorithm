import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())

c_map = []
for i in range(N):
    line = input()
    line_list = []
    for c in line:
        if c !='\n':
            line_list.append(c)
    c_map.append(line_list)

def check_all(c_map):
    answer = 0
    for r in range(N):
        for c in range(N):
            pos = c_map[r][c]

            #case1
            cnt = 1
            while c+cnt < N:
                if c_map[r][c+cnt] == pos:
                    cnt += 1
                else: break
            if cnt > answer:
                answer = cnt

            #case2
            cnt = 1
            while r+cnt < N:
                if c_map[r+cnt][c] == pos:
                    cnt += 1
                else: break
            if cnt > answer:
                answer = cnt
    
    return answer


def check(c_map, type, pos):
    answer = 0
    r,c = pos
    if type == 'r':
        # 행 조사
        for i in range(N-1):
            cnt = 1  
            for j in range(i+1, N):
                if c_map[r][i] == c_map[r][j]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt

            cnt = 1  
            for j in range(i+1, N):
                if c_map[r+1][i] == c_map[r+1][j]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt

            cnt = 1  
            for j in range(i+1, N):
                if c_map[i][c] == c_map[j][c]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt
        
    else:
        # 열 조사
        for i in range(N-1):
            cnt = 1  
            for j in range(i+1, N):
                if c_map[i][c] == c_map[j][c]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt

            cnt = 1  
            for j in range(i+1, N):
                if c_map[i][c+1] == c_map[j][c+1]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt

            cnt = 1  
            for j in range(i+1, N):
                if c_map[r][i] == c_map[r][j]:
                    cnt +=1
                else : break
            if cnt > answer:
                answer = cnt

    return answer

answer = check_all(c_map)
for r in range(N):
    for c in range(N):
        pos = [r,c]
        # case 1
        if c < N-1:
            # c_map_1 = deepcopy(c_map)
            c_map[r][c], c_map[r][c+1] = c_map[r][c+1], c_map[r][c]
            max_len = check(c_map, "c", pos)
            if max_len > answer:
                answer = max_len

            c_map[r][c], c_map[r][c+1] = c_map[r][c+1], c_map[r][c]
            
        # case 2
        if r < N-1:
            # c_map_2 = deepcopy(c_map)
            c_map[r+1][c], c_map[r][c] = c_map[r][c], c_map[r+1][c]
            max_len = check(c_map, "r", pos)

            if max_len > answer:
                answer = max_len

            c_map[r+1][c], c_map[r][c] = c_map[r][c], c_map[r+1][c]
            


print(answer)