X = int(input(''))
L = 64

sticks = []
while sum(sticks) != X:
    if L == X-sum(sticks):
        sticks.append(L)
        break
    elif L < X-sum(sticks):
        sticks.append(L)
    L /= 2

print(len(sticks))