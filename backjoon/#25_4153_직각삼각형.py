# line = input('')
# tri_len = [list(map(int,line.split(' ')))]
tri_len=[]
while True:
    line = input('')
    if line == '0 0 0':
        break
    tri_len.append(list(map(int,line.split(' '))))



for t in tri_len:
    t.sort()
    if t[0]**2 + t[1]**2 == t[2]**2:
        print("right")
    else:
        print("wrong")
