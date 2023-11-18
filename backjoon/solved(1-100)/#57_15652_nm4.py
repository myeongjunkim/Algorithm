from itertools import combinations_with_replacement

N, M = map(int, input('').split(' '))
num_list = list(range(1,N+1))
case_list = list(map(list,combinations_with_replacement(num_list,M)))

for case in case_list:
    for el in case:
        print(el, end=' ')
    print("")
