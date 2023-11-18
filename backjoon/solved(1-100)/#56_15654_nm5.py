from itertools import permutations

N, M = map(int, input('').split(' '))

num_list = list(map(int, input('').split(' ')))
num_list.sort()

case_list = list(map(list,permutations(num_list,M)))

for case in case_list:
    for el in case:
        print(el, end=' ')
    print("")