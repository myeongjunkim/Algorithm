"""
이진탐색 201p

떡개수, 요청한 떡 길이
4 6
19 15 10 17
->15
"""

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort()
long_rice = rice[-1]

def find_l(start, end):
    while start <= end:
        m = (start+end)// 2
        res = is_target(m)

        if res == 0:
            return m
        elif res == 1:
            start = m +1
        elif res == -1:
            end = m-1
    return None

def is_target(m):
    sum_l = 0
    for r in rice:
        if r>m:
            sum_l += r-m
    
    if sum_l == L:
        return 0
    elif sum_l > L:
        return 1
    else:
        return -1

print("%2f")

print(find_l(1,long_rice))