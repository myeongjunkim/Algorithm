"""
큰 수의 법칙(이코테 page 92)

ex)
5 8 3
2 4 5 4 6

"""

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse = True)

cnt = 0
res = 0
flag = True
for i in range(M):
	cnt += 1
	if flag: addition = nums[0]
	else: addition = nums[1]
	res+=addition
	if cnt == 3:
		flag = False
		cnt = -1
	else: flag = True
print(res)

# 16 m