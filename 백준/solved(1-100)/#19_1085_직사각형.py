line = list(map(int,input('').split(' ')))
x, y, w, h = line[0], line[1], line[2], line[3]

print(min(w-x,x, h-y, y))