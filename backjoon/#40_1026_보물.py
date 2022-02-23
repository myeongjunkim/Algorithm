import sys
N = int(input(''))

list_a = list(map(int,sys.stdin.readline().strip().split(' ')))
list_b = list(map(int,sys.stdin.readline().strip().split(' ')))

list_a.sort()
list_b.sort(reverse=True)

sum = 0
for i in range(N):
    sum += list_a[i] * list_b[i]

print(sum)