def check_section(M,N, points):
    first_point = points.pop()
    X, Y = first_point[0], first_point[1]

    section = [[X, Y]]
    while len(section) != 0:
        new_point = section.pop()
        X,Y = new_point[0], new_point[1] 

        if X != 0:
            if [X-1, Y] in points:
                points.remove([X-1, Y])
                section.append([X-1, Y])
        if X != M-1:
            if [X+1, Y] in points:
                points.remove([X+1, Y])
                section.append([X+1, Y])
        if Y != 0:
            if [X, Y-1] in points:
                points.remove([X, Y-1])
                section.append([X, Y-1])
        if Y != N-1:
            if [X, Y+1] in points:
                points.remove([X, Y+1])
                section.append([X, Y+1])

    return points



def get_cnt(M, N, points):
    cnt = 0
    while len(points) != 0:
        points = check_section(M,N, points)
        cnt += 1
        
    return cnt       

T = int(input(''))

result=[]
for i in range(T):
    line = list(map(int,input('').split(' ')))
    M, N, cnt = line[0], line[1], line[2]
    points=[]
    for j in range(cnt):
        points.append(list(map(int,input('').split(' '))))
    result.append(get_cnt(M, N, points))

for r in result:
    print(r)


