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

    str.find(sub_string)
        -> KMP 문자열 검색 알고리즘
    str.zfill(n)
        -> 문자열 길이가 n이 되도록 앞부분을 0 으로 채우기
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

2. 딕셔너리
    
    ```
    a = defaultdict(list)
    -> 키 셋팅 필요 없이 모든 키에 대한 초기값을 list 로 지정

    ex) a["asdfas"].append("dfdfs") -> "asdfas" 키를 선언하지 않아도 Key 에러가 나지 않음
    ```
    
3. 큐

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


## Python 알고리즘

1. DFS 깊이우선 탐색 알고리즘
2. BFS 너비우선 탐색 알고리즘

    ```
    거리 -> dist 리스트를 선언하고 이전 node 의 dist 값을 하나씩 늘려가며 기록
    경로 -> pre_node 리스트를 선언하고 이전 node 의 위치를 기록
    범위 -> not (0 <= r < N and 0 <= c < M) 를 통해 분기 처리
    방문 -> 인접 노드(new_r, new_c)를 q 에 추가할 때 방문 처리 ( pop 할 때 방문처리 하면 경우에 따라 메모리 초과 이슈 발생 )
    ```
    
4. DP 다이나믹 프로그래밍 알고리즘
    
    ```
    dp 배열 선언 -> 1, 2, 3 차원 배열을 통해 기록
    ```
    
5. Dijkstra 다익스트라 알고리즘
6. 벨만포드 알고리즘
7. Prime, Kruskal 알고리즘
        
    [Prim MTS]
    ```
    시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법

    정점 선택을 기반으로 하는 알고리즘이다.
    이전 단계에서 만들어진 신장 트리를 확장하는 방법이다.
    
    1. 시작 단계에서는 시작 정점만이 MST(최소 비용 신장 트리) 집합에 포함된다.
    2. 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
        즉, 가장 낮은 가중치를 먼저 선택한다.
    3. 위의 과정을 트리가 (N-1)개의 간선을 가질 때까지 반복한다.
    ```
   
    [Kruskal MTS]
    ```
    탐욕적인 방법(greedy method) 을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것
   
    MST(최소 비용 신장 트리) 가
    1) 최소 비용의 간선으로 구성됨
    2) 사이클을 포함하지 않음
    의 조건에 근거하여 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택 한다.
    간선 선택을 기반으로 하는 알고리즘이다.
    이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최소 간선만을 선택하는 방법이다.

    1. 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
    2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
        즉, 가장 낮은 가중치를 먼저 선택한다.
        사이클을 형성하는 간선을 제외한다.
    3. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
    ```
    -> 우선순위 큐 또는 최소힙을 사용해 가장 낮은 간선을 찾을 수 있다.
   
8. KMP 알고리즘
9. 위상정렬 알고리즘
