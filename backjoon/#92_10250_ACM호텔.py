import sys
input = sys.stdin.readline

N = int(input())


case = []
for i in range(N):
	case.append(map(int, input().split()))

for c in case:
	H, W, n = c
	level = n%H
	if level == 0: 
		level = H
		room = n//H
	else:
		room = n//H +1
	if room < 10: room = "0" + str(room)
	print(f"{level}{room}")


	# H로 나눈 나머지 -> 층수
	# H로 나눈 몫 + 1-> 호수 

