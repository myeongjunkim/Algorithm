import sys
num=sys.stdin.readlines()

sys.setrecursionlimit(10**6)

T = int(input(''))

num_list = [int(sys.stdin.readline().strip()) for i in range(T)]

points = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(T)]



from collections import deque
queue = deque([4, 5, 6])
queue.append(7)
queue.appendleft(7)
queue.pop()
queue.popleft()
queue.extend([1,2,3])
queue.extendleft([1,2,3])
deque.remove(1)


# from queue import PriorityQueue
# Q = PriorityQueue()
# # 원소 삽입
# Q.put(데이터)
# Q.put((우선순위, 데이터))
# # 원소 삭제 - 우선순위 높은 순서대로 삭제
# Q.get() 
# Q.get()[1]


# 최소힙. 오름차순 자동 정렬함
from heapq import heappush
from heapq import heappop
from heapq import heapify

heap = []
heappush(heap, 4)
heappop(heap)

num_list = [1,2,3,4]
heapify(num_list)



# 람다 정렬
points= sorted(points, key = lambda x : (x[1],x[0]))



def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result


# 순열과 조합
from itertools import permutations, product, combinations, combinations_with_replacement

print(list(product([1,2,3,4], repeat=2)))
print(list(permutations([1,2,3,4], 2)))
print(list(combinations([1,2,3,4], 2)))
print(list(combinations_with_replacement([1,2,3,4], 2)))




# 문자열 판단
str.isdigit()
str.isalpha()
str.upper()
str.lower()
str.isupper()
str.islower()


# 집합
a={1,2,3}
a.remove(2)
a.discard(3)
a.add(1)