# https://jennnn.tistory.com/60

import sys
input = sys.stdin.readline

target = input().strip()
N = int(input())

broken = list(map(int,input().split()))

res = abs(int(target)-100)



for num in range(1000001):

    is_there = False
    for n in str(num):
        if int(n) in broken:
            is_there = True
            break
    if not is_there:
        res = min(res, len(str(num)) + abs(int(target) - num))



print(res)