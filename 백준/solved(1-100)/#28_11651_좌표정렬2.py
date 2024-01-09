
import sys
T = int(input(''))
points = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(T)]

points= sorted(points, key = lambda x : (x[1],x[0]))

for point in points:
    print(point[0], point[1])
