
import sys
M, N = map(int, sys.stdin.readline().strip().split(' '))

decimal = []
if int(N**0.5) >= 2:
    for i in range(2,int(N**0.5)+1):
        flag=True
        for j in range(2,i):
            if i%j == 0:
                flag=False
                break
        if flag:
            decimal.append(i)
            if i>= M:
                print(i)


for i in range(M, N+1):
    flag=True
    for d in decimal:
        if i%d == 0:
            flag=False
            break
    if flag and i !=1:
        print(i)


    
