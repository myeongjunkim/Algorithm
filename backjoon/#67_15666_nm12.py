import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(set((map(int, input().split()))))
num_list.sort()

case_list = list(combinations_with_replacement(num_list, m))

for r in case_list:
    for n in r:
        print(n, end=" ")
    print("")