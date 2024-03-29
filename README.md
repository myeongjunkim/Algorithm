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

5. 올림, 내림

    ```
    import math

    math.ceil(-3.14)    # -3
    math.ceil(3.14)     # 4
    
    math.floor(3.14)    # 3
    math.floor(-3.14)   # -4
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

7. zip()

    ```
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for pair in zip(numbers, letters):
        print(pair)
    
    (1, 'A')
    (2, 'B')
    (3, 'C')
    ```

8. bisect 이진 탐색

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

1. 리스트

    ```
    a = [0,1,2,3,4,5]

    a.pop()          
    a.pop(index)      
    a.remove(value)
    del a[index)
    a.insert(1, 10)   # 두 번째위치에 10 삽입  
    a.index(value)
    a.append(value)
    a.count(value)
    a.extend([4,5,6])
 
    a = [[1, 2], [3, 4]]
    b = [item[:] for item in a]  # deapcopy 대신 사용 가능

    a = [[1, 10], [2, 22], [3, 19], [4, 7]]
    b = sum(list1, [])                       # list1 의 요소들을 [] 에 반복하여 더한다.
    >> [1, 10, 2, 22, 3, 19, 4, 7]
    ```

3. 집합

    ```
    a = {1,2,3}
    
    a.remove(2) # 있는 것 제거, 없으면 index 에러
    a.discard(3) # 없어도 에러 x
    a.add(1)
    set1 & set2
    set1 | set2


    line = "hello"
    set_line = set(line) 
    -> {'e', 'h', 'l', 'o'}
    ```
    
4. 비트마스크
    
    ```
    &	AND 연산. 비교하는 비트가 둘 다 참일 때만 만족
    |	OR 연산. 비교하는 비트가 둘 중 하나라도 참이면 만족
    ^	XOR 연산. 비교하는 비트가 둘 중 하나만 참일때만 만족
    ~	NOT 연산. 보수 연산으로 0 -> 1, 1 -> 0
    <<	왼쪽 시프트 연산. 변수의 값을 지정된 값의 비트만큼 왼쪽으로 이동
    >>	오른쪽 시프트 연산. 변수의 값을 지정된 값의 비트만큼 오른쪽으로 이동
    ```
    -> int type 에 사용 가능
    -> bin() 결과값은 str type 이므로 사용 불가
   
 

5. 딕셔너리
    
    ```
    a = defaultdict(list)
    -> 키 셋팅 필요 없이 모든 키에 대한 초기값을 list 로 지정

    ex) a["asdfas"].append("dfdfs") -> "asdfas" 키를 선언하지 않아도 Key 에러가 나지 않음
    ```
    
6. 큐

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

   ```
   visited = [[False] * C for _ in range(R)]  

   def dfs(r, c):
       global visited
   
       visited[r][c] = True
       for dr, dc in [(1,0), (-1,0), (0,-1), (0,1)]:
           new_r, new_c = r + dr, c + dc
           if not (0<=new_r<R and 0<=new_c<C)
               continue
           if visited[new_r][new_c]:
               continue
           if _map[new_r][new_c]:
               continue
           dfs(new_r, new_c)
   ``` 

3. BFS 너비우선 탐색 알고리즘

   ```
   def bfs(start):
       R, C = len(_map), len(_map[0])
       visited = [[0] * C for _ in range(R)]
       pre_node = [[ (-1,-1) for _ in range(C) ] for _ in range(R)]
       q = deque([start])
       while q:
           r, c = q.popleft()
           for dr, dc in [(1,0), (-1,0), (0,-1), (0,1)]:
               new_r, new_c = r + dr, c + dc
               if not (0<=new_r<R and 0<=new_c<C)
                   continue
               if visited[new_r][new_c] or (new_r, new_c) == start:
                   continue
               if _map[new_r][new_c]:
                   continue
               q.append((new_r, next_c))
               visited[new_r][new_c] = visited[r][c] + 1
               pre_node[new_r][new_c] = (r, c)
        
   ```
   ```
    거리 -> visited 리스트를 선언하고 이전 node 의 visited 값을 하나씩 늘려가며 기록 
            ( 시작 node 의 visited 값은 0 이기 때문에 예외처리 또는 시작을 1 로 두고 결과에 보정)
            ( 만약 visited 값이 변경될 여지가 있다면 q 의 데이터 구조를 (r,c,dist) 로 가져간다 )
    경로 -> pre_node 리스트를 선언하고 이전 node 의 위치를 기록
    범위 -> not (0 <= r < N and 0 <= c < M) 를 통해 분기 처리
    방문 -> 인접 노드(new_r, new_c)를 q 에 추가할 때 방문 처리 ( pop 할 때 방문처리 하면 경우에 따라 메모리 초과 이슈 발생 )
   ```
    
4. BFS/DFS 를 통한 클러스터링
    ```
    def bfs(r,c, id):
        _map[r][c] = id
        q = deque([(r,c)])
        result = []
        while q:
          r, c = q.popleft()
          result.append((r, c))
          for dr, dc in [ (1,0), (-1,0), (0,1), (0,-1) ]:
            new_r, new_c = r+dr, c+dc
            if not (0<=new_r<N and 0<=new_c<M):
              continue
            if _map[new_r][new_c]:
              continue
            q.append((new_r, new_c))
            _map[new_r][new_c] = id
        return result

    def cluster()
      id_map = {}
      id = 1
      for r in range(N):
        for c in range(M):
          if _map[r][c] == 0:
            id += 1
            result = bfs(_map, r,c, id)
            id_map[id] = result
      return id_map
    ```
    ```
        1. 모든 노드를 순회하면서 0 인 노드를 찾는다.
        2. BFS 또는 DFS 를 통해 이를 시작점으로 하는 군집을 리턴한다.
        3. cluster 함수에서 각 id 별 군집을 기록한다.
    ```
    


5. DP 다이나믹 프로그래밍 알고리즘
    
    ```
    dp 배열 선언 -> 1, 2, 3 차원 배열을 통해 기록
    ```
    
6. Dijkstra 다익스트라 알고리즘

    ```
    INF = int(1e9)
    
    def dijkstra(start, _map):
        dist = [INF]*len(_map)
        
        dist[start] = 0
        heap = [ (0,start) ]
        while heap:
            pos_dist, pos_n = heappop(heap)
            
            if pos_dist > dist[pos_n]: # pop 되기 전에 다른 노드로 인해 최단거리가 업데이트된 상황
                continue
            for next_w, next_n in _map[pos_n]:
                if dist[next_n] > dist[pos_n]+next_w:
                    dist[next_n] = dist[pos_n]+next_w
                    heappush( heap, (dist[next_n], next_n) )
        return dist
    ```
    ```
    방문 -> 체크하지 않는다
    dist -> start 에서 각 노드까지 최단거리를 기록하고 업데이트 한다.
    
    ```
    
7. Bellman Ford 벨만포드 알고리즘
    
    ```
    def BF(start, N, lines): 
      dist = [sys.maxsize]*(N+1)
      dist[start] = 0
      
      for i in range(N):
        for a, b, w in _map
          if dist[a] != sys.maxsize and dist[b] > dist[a] + w:
            dist[b] = dist[a] + w
            if i == N-1:
              return []
      
      return dist

    ```
    ```
    결과 -> dist 반환: 순환고리 x // [] 반환: 순환고리: o
    ```

8. Floyd Warshall 플로이드 워셜 알고리즘

    ```
    def floyd_warshall(_map, n)
        dp = [[INF] * (n+1) for _ in range(n+1)]

        for n1 in range(1, n+1):
            dp[n1][n1] = 0
            for w, n2 in _map[k]:
                dp[n1][n2] = w
    
        for k in range(1, n+1): # via
            for i in range(1, n+1): # start
                for j in range(1, n+1): # end
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

        return dp
    ```
    ```
    조건 -> 사이클이 없는 것 전제
    ```

9. Prime, Kruskal 프림, 크루스칼 알고리즘
        
    [Prim MTS]

    ```
    from heapq import heapify, heappush, heappop

    def prim(N, _map):
        mst = []
        visited = [False]*(N+1)
    
        heap = [ (0,0,1) ]
        while heap:
            w, start_n, end_n = heappop(heap)
            if visited[end_n]:
                continue
            visited[end_n] = True
            mst.append((w, start_n, end_n))
    
            for next_w, next_n in _map[end_n]:
                if visited[next_n]:
                    continue
                heapq.heappush(heap, (next_w, end_n, next_n))

        return mst
    ```

    ```
    시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법

    정점 선택을 기반으로 하는 알고리즘이다.
    이전 단계에서 만들어진 신장 트리를 확장하는 방법이다.
    
    1. 시작 단계에서는 시작 정점만이 MST(최소 비용 신장 트리) 집합에 포함된다.
    2. 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
        즉, 가장 낮은 가중치를 먼저 선택한다.
    3. 위의 과정을 트리가 모든 연결 정점을 돌 때 까지 반복한다.
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
   
10. Topology Sort 위상정렬 알고리즘

    ```
    from collections import deque

    
    def topology_sort(N, _map):
        indegree = [0] * (N + 1)
        for _ in range(N+1):
            for b in _map[a]:
                indegree[b] += 1
    
        result = []
        q = deque( [n for n in range(1, N+1) if indegree[i] == 0] )
        while q:
            pos_n = q.popleft()
            result.append(pos_n)
            for next_n in _map[pos_n]:
                indegree[next_n] -= 1
                if indegree[next_n] == 0:
                    q.append(next_n)
    ```
    
12. Union-Find 유니온 파인드 알고리즘

    ```
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x
    
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    ```
