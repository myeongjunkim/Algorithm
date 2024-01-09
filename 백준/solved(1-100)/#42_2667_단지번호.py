import sys

def get_nearby(one_point_index, point, map):
    r, c, N = point[0], point[1], len(map)
    nearby=[]
    if r != 0 and [r-1,c] in one_point_index:
        nearby.append([r-1,c])
        one_point_index.remove([r-1,c])
    if r != N-1 and [r+1,c] in one_point_index:
        nearby.append([r+1,c])
        one_point_index.remove([r+1,c])
    if c != 0 and [r,c-1] in one_point_index:
        nearby.append([r,c-1])
        one_point_index.remove([r,c-1])
    if c != N-1 and [r,c+1] in one_point_index:
        nearby.append([r,c+1])
        one_point_index.remove([r,c+1])

    return nearby, one_point_index

N = int(input(''))

map=[]
one_point_index=[]
for r in range(N):
    line = sys.stdin.readline().strip()
    line_list=[]
    for c in range(N):
        n = int(line[c])
        line_list.append(n)
        if n:
            one_point_index.append([r,c])
    map.append(line_list)





# 1 있는 index 다 모으기
# 하나씩 pop,  스텍에 넣고
# 스텍에서 하나 뽑아서 인접 한 포인트가 1인지 확인(one_point_index여기 에 있는지)후
#  1인 인덱스 모아서 뭉치고 one_point_index에서 제거, 스텍에 넣기


section_list=[]
while one_point_index:
    point = one_point_index.pop()
    nearby, one_point_index = get_nearby(one_point_index, point, map)
    section=[point]
    section.extend(nearby)
    while nearby:
        point = nearby.pop()
        nearby_plus, one_point_index = get_nearby(one_point_index, point, map)
        for p in nearby_plus:
            if p not in nearby:
                nearby.append(p)
                section.append(p)      

    
    section_list.append(section)

section_list = sorted(section_list, key=lambda x:len(x))

print(len(section_list))
for section in section_list:
    print(len(section))