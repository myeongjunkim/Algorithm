# 시작점이 a,b 일 때 8 8 보드판 ㄹ 자로 잇기
def make_oneline(board,a,b):
    one_line = ""
    for i in range(8):
        if i%2 == 0:
            one_line += board[b+i][a:a+8]
        else:
            one_line += board[b+i][a:a+8][::-1]
    return one_line


def overlap_cnt(one_line):
    W_start, B_start = 0, 0
    for i in range(64):
        if i%2 == 0:
            if one_line[i] == 'B':
                W_start +=1 
            else:
                B_start +=1
        else:
            if one_line[i] == 'W':
                W_start += 1
            else:
                B_start += 1
    
    return min(W_start, B_start)


# main
m_n = list(map(int, input().split()))
M, N = m_n[0], m_n[1]

all_min=[]
board=[]
for i in range(M):
    board.append(input())


for a in range(0,N-8+1):
    for b in range(0,M-8+1):
        one_line = make_oneline(board,a,b)
        one_line_min = overlap_cnt(one_line)
        all_min.append(one_line_min)

if len(all_min) == 1:
    print(all_min[0])
else:
    print(min(all_min))