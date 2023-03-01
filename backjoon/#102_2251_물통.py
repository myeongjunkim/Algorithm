
# https://cijbest.tistory.com/14

import sys
from collections import deque
input= sys.stdin.readline


A, B, C = map(int, input().split())

def execute():

    visited = [[False]*(B+1) for _ in range(A+1)]
    q = deque()

    visited[0][0] = True
    q.append((0, 0, C))
    res = [C]
    while q:
        next_case = get_next_case(q.popleft())
        for case in next_case:
            a, b, c = case
            if not visited[a][b]:
                visited[a][b] = True
                if a==0:
                    res.append(c)
                q.append(case)

    print(" ".join(list(map(str, sorted(res)))))

def get_next_case(case):
    """
    case = [a, b, c]
    a -> b
    a -> c
    b -> a
    b -> c
    c -> a
    c -> b
    """
    res = []
    a, b, c = case

    if a:
        new_a, new_b, new_c = water(a, b, c, B)
        res.append((new_a, new_b, new_c))
        new_a, new_c, new_b = water(a, c, b, C)
        res.append((new_a, new_b, new_c))

    if b:
        new_b, new_a, new_c = water(b, a, c, A)
        res.append((new_a, new_b, new_c))
        new_b, new_c, new_a = water(b, c, a, C)
        res.append((new_a, new_b, new_c))

    if c:
        new_c, new_a, new_b = water(c, a, b, A)
        res.append((new_a, new_b, new_c))
        new_c, new_b, new_a = water(c, b, a, B)
        res.append((new_a, new_b, new_c))
    
    return res
    
def water(x, y, z, max_y):
    # x -> y
    new_x = x+y - max_y if x+y>max_y else 0
    new_y = max_y if x+y>max_y else x+y
    new_z = z
    return new_x, new_y, new_z




execute()