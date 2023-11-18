import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
N_sum = 0
i = 1
while True:
    N -= i
    i +=1
    if N < 0: break
    cnt += 1
    
print(cnt)