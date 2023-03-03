import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split()))

hash={}
for n in nums:
    try:
        hash[n] += 1
    except Exception:
        hash[n] = 1

for n in find_nums:
    try:
        print(hash[n])
    except:
        print(0)
