import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

case_list = list(set(permutations(num_list, m)))
case_list.sort()

for case in case_list:
    for c in case:
        print(c, end=" ")
    print("")