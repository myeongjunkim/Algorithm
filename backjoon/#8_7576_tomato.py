def is_complete(data):
    for line in data:
        for d in line:
            if d == 0:
                return 0
    return 1


def to_change(data, index_plus, M, N):
    new_index_plus=[]
    while len(index_plus) != 0:
        m_n = index_plus.pop()
        if m_n[0] != 0:
            if data[m_n[0]-1][m_n[1]] == 0:
                new_index_plus.append([m_n[0]-1,m_n[1]])
                data[m_n[0]-1][m_n[1]] = 1
        if m_n[0] != M-1:
            if data[m_n[0]+1][m_n[1]] == 0:
                new_index_plus.append([m_n[0]+1,m_n[1]])
                data[m_n[0]+1][m_n[1]] = 1
        if m_n[1] != 0:
            if data[m_n[0]][m_n[1]-1] == 0:
                new_index_plus.append([m_n[0],m_n[1]-1])
                data[m_n[0]][m_n[1]-1] = 1
        if m_n[1] != N-1:
            if data[m_n[0]][m_n[1]+1] == 0:
                new_index_plus.append([m_n[0],m_n[1]+1])
                data[m_n[0]][m_n[1]+1] = 1
    return new_index_plus


def get_index(data):
    index_plus = []
    m = 0
    for line in data:
        n = 0
        for d in line:
            if d == 1:
                index_plus.append(([m,n]))
            n +=1
        m+=1
    return index_plus


N, M = map(int,input('').split(' '))
data = []
for i in range(M):
    data.append(list(map(int,input('').split(' '))))
index_plus = get_index(data)

if is_complete(data):
    print(0)

else:
    cnt = 0
    while len(index_plus) != 0:
        index_plus = to_change(data, index_plus, M, N)
        if len(index_plus) != 0:
            cnt +=1

    if is_complete(data):
        print(cnt)
    else:
        print(-1)