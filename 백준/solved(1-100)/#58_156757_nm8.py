from itertools import combinations_with_replacement

N, M = input('').split(' ')

num_list = list(map(int, input('').split(' ')))
num_list.sort()

case_list = list(map(list, combinations_with_replacement(num_list, int(M))))

for case in case_list:
    for el in case:
        print(el, end=' ')
    print('')