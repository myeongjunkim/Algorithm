import sys

def get_nearby(point, map):
    nearby = []
    r, c, N = point[0], point[1], len(map)
    if r != 0 and map[r][c] == map[r-1][c]:
        nearby.append([r-1,c])
    if r != N-1 and map[r][c] == map[r+1][c]:
        nearby.append([r+1,c])
    if c != 0 and map[r][c] == map[r][c-1]:
        nearby.append([r,c-1])
    if c != N-1 and map[r][c] == map[r][c+1]:
        nearby.append([r,c+1])
    return nearby


def get_section_cnt(_index, map):
    cnt = 0
    while _index:
        head = _index.pop()
        section = [head]
        while section:
            point = section.pop()
            nearby = get_nearby(point, map)
            for p in nearby:
                if p in _index:
                    _index.remove(p)
                    if p not in section:
                        section.append(p)
        cnt += 1
    return cnt

# main
N = int(input(''))

R_index=[]
G_index=[]
B_index=[]

map = []
for r in range(N):
    line = sys.stdin.readline().strip()
    map.append(line)
    for c in range(N):
        if line[c] == "R":
            R_index.append([r,c])
        elif line[c] == "G":
            G_index.append([r,c])
        elif line[c] == "B":
            B_index.append([r,c])

new_map = []
R_index_2=[]
B_index_2=[]
for r in range(N):
    line = ""
    for c in range(N):
        if map[r][c] == "R" or map[r][c] == "G":
            R_index_2.append([r,c])
            line +="R"
        elif map[r][c] == "B":
            B_index_2.append([r,c])
            line +="B"
    new_map.append(line)

result_1 = get_section_cnt(R_index, map) + get_section_cnt(G_index, map) + get_section_cnt(B_index, map)
result_2 = get_section_cnt(R_index_2,new_map) + get_section_cnt(B_index_2, new_map)
print(result_1, result_2)