"""
문제 풀이 방법

1. N, M을 정수로 받는다
2. N개의 카드 목록을 받아 
3. 역순으로 정렬한다
4. M보다 작을때까지 더한다.
	커지면 그 전에 더한 숫자를 찾는다
    세 수의 합을 찾는다
5. 기존 것보다 크면 값 체인지

"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))


# solve 1
def find_num():
	large_num = num_list[0] + num_list[1] + num_list[2]
	for i in range(len(num_list)-2):
		for j in range(i+1, len(num_list)-1):
			for k in range(j+1, len(num_list)):

				pos = num_list[i] + num_list[j] + num_list[k]
				if pos > M:
					continue
				else:
					large_num = max(large_num, pos)
					
	return large_num

print(find_num())


# solve 2

large_num = 0
for pos in combinations(num_list, 3):
	sum_num = sum(pos)
	if large_num < sum_num <= M:
		large_num = sum_num

print(large_num)
        


                
    
