
import sys
input = sys.stdin.readline

N = int(input())

points = []
for line in range(N):
	points.append(list(map(int, input().split())))

sorted_points = sorted(points, key = lambda x : (x[0],x[1]))

for point in sorted_points:
	print(point[0], point[1])