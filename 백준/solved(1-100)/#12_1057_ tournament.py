
def to_half(N):
    if N%2 !=0:
        N +=1
    return N/2

line = list(map(int,input('').split(' ')))
line.sort()
kim, lim, N = line[0], line[1], line[2]

cnt = 1
while True:
    if lim - kim == 1 and lim %2 == 0:
        break
    else:
        N, kim, lim = to_half(N), to_half(kim), to_half(lim)
        cnt +=1
    
print(cnt)