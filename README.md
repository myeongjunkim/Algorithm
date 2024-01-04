# Algorithm

## Python 셋팅

1. input 셋팅

    ```
    import sys

    input=sys.stdin.readline
    ```

2. recursion 셋팅

    ```
    import sys

    sys.setrecursionlimit(10**6)
    ```

3. max num 셋팅

    ```
    import sys

    ans = sys.maxsize
    ```

## Python 입출력

1.  N*M 입력

    ```
    3
    1 2 3
    4 5 6
    7 8 9

    MAP = [list(map(int, input().split())) for _ in range(int(input()))]
    ```

2. N - numlist 입력
    ```
    4 10 20 30 40
    3 7 5 12
    3 125 15 25

    N, *arr = map(int, input().split())
    ```
    
3. 문자열 입력
    ```
    3
    AAAA 
    ABCA 
    AAAA
    
    arr = [list(input()) for _ in range(N)]
    ```


4. 리스트 출력

    ```
    arr = [1, 2, 3, 4] 
    
    print("".join(map(str, arr)))   # "1234"
    print(*arr)     # "1 2 3 4"

    ```


## Pytnon 메소드


1. 문자열

    ```
    str.isdigit()
    str.isalpha()
    str.isupper()
    str.islower()
    str.upper()
    str.lower()
    ```



2. 리스트 원소 개수

    ```
    list.count(찾는 값)
    ```

    ```
    from collections import Counter 

    Counter(arr).most_common()  # [(원소, 개수), (원소, 개수),,, ] 최빈값 순
    ```


3. 정렬


    ```
    points = sorted(points, key = lambda x : (x[1],x[0]))
    ```

    ```
    arr.sort(reverse=True)  # 내림차순 정렬
    arr.reverse()   # 역순
    str[::-1]   # 역순
    ```

4. 순열과 조합

    ```
    from itertools import permutations, product, combinations, combinations_with_replacement

    list(permutations([1,2,3,4], 2))
    list(combinations([1,2,3,4], 2))
    list(product([1,2,3,4], 2))
    list(combinations_with_replacement([1,2,3,4], 2))
    ```

5. Factorial

    ```
    def factorial(n):
        result = 1
        for i in range(1,n+1):
            result*=i
        return result
    ```

6. enumerate

    ```
    item = ["First", "Second", "Third"] 
    for i, val in enumerate(item): 
    	print(f"{i} 번쨰 값은 {val}입니다") 


    0 번쨰 값은 First입니다 
    1 번쨰 값은 Second입니다 
    2 번쨰 값은 Third입니다 
    ```

7. bisect 이진 탐색

    ```
    from bisect import bisect_right, bisect_left

    lst= [1, 4, 6, 10]
    
    print(bisect_left(lst, 6)) # result = 2
    print(bisect_right(lst , 6)) # result = 3
        
    print(bisect_left(lst, 9)) # result = 3
    print(bisect_right(lst , 9)) # result = 3

    1. 해당 값이 리스트에 있을 때
    
    bisect_left - 해당 index 반환
    bisect_right - 해당 index+1 반환
    

    2. 해당 값이 리스트에 없을 때
    
    bisect_left - 리스트 오름차순에 들어갈 index 반환
    bisect_right - 리스트 오름차순에 들어갈 index 반환

    ```


## Python 자료구조

1. 집합

    ```
    a = {1,2,3}

    a.remove(2)
    a.discard(3)
    a.add(1)
    set1 & set2
    set1 | set2


    line = "hello"
    set_line = set(line) 
    -> {'e', 'h', 'l', 'o'}
    ```

2. 큐

    ```
    from collections import deque
    
    queue = deque([4, 5, 6])
    
    queue.append(7)
    queue.appendleft(7)
    
    queue.pop()
    queue.popleft()

    queue.rotate(1)
    queue.rotate(-1)
    
    queue.extend([1,2,3])
    queue.extendleft([1,2,3])
    
    queue.remove(1)
    ```

3. 우선순위 큐

    ```
    from queue import PriorityQueue
    
    Q = PriorityQueue()
    
    Q.put(데이터)
    Q.put((우선순위, 데이터))
    
    Q.get() # 우선순위 높은 순서대로 get
    Q.get()[1] 
    ```

4. 최소힙

    ```
    from heapq import heappush
    from heapq import heappop
    from heapq import heapify

    heap = []
    heappush(heap, 4)
    heappop(heap)

    num_list = [1,2,3,4]
    heapify(num_list)
    ```
