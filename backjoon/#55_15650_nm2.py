from itertools import combinations

N, M = map(int, input('').split(' '))

n_list = list(range(1,N+1))

case_list = list(map(list,combinations(n_list,M)))

for case in case_list:
    for el in case:
        print(el, end=' ')
    print("")




