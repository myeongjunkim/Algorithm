from collections import deque
import sys
T = int(input(''))

test_case = []
for i in range(T):
    num_list = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(2)]
    test_case.append(num_list)

result = []
for case in test_case:
    target_index = case[0][1]
    queue = deque(case[1])
    point_list = list(range(case[0][0]))
    point_index = 0
    rank = 0
    while queue:
        num = queue.popleft()
        if not queue:
            rank +=1
            result.append(rank)
            break
        elif num >= max(queue):
            rank +=1
            point_index = (point_index)%len(point_list)
            if point_list[point_index] == target_index:
                result.append(rank)
                break
            else:
                del point_list[point_index]

        else:
            queue.append(num)
            point_index = (point_index+1)%len(point_list)



for r in result:
    print(r)