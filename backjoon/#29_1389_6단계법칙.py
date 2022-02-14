import sys
N_M = list(map(int,sys.stdin.readline().strip().split(' ')))
N, M = N_M[0], N_M[1]

points = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(M)]

relationship = {}
for point in points:
    user, f = point[0], point[1]
    try:
        relationship[user] += [f]
    except KeyError:
        relationship[user] = [f]

    try:
        relationship[f] += [user]
    except KeyError:
        relationship[f] = [user]

# print(relationship)
kb_list = []
for k in sorted(list(relationship.keys())):

    f_list = relationship[k]
    # print("f리스트",f_list)
    kb_num = 0
    for i in range(1,N+1):
        stack = set(f_list)
        cnt = 1
        if i != k:
            while i not in stack:
                cnt += 1
                new_stack = []
                for f in stack:
                    if i in relationship[f]:
                        new_stack = relationship[f]
                        break
                    else:
                        new_stack += relationship[f]
                stack = set(new_stack)
            # print(i, cnt)
            kb_num += cnt

    # print(k,"의 숫자:", kb_num)
    if kb_num not in kb_list:
        kb_list.append(kb_num)
        if min(kb_list) == kb_num:
            kb_man = k

print(kb_man)
    
