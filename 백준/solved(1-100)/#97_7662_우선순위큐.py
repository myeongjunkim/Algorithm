import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def execute():
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        validation = [True]*N
        heap_min = []
        heap_max = []
        for id in range(N):
            line = input().split()
            cmd, n = line[0], int(line[1])
            if cmd == "D":
                if n == 1:
                    flag = False
                    while not flag:
                        if heap_max:
                            num ,id = heappop(heap_max)
                            flag = validation[id]
                        else:
                            flag = True
                    validation[id] = False
                elif n == -1:
                    flag = False
                    while not flag:
                        if heap_min:
                            num ,id = heappop(heap_min)
                            flag = validation[id]
                        else:
                            flag = True
                    validation[id] = False
                else:
                    print("not case")
            elif cmd == "I":
                heappush(heap_min, (n, id))
                heappush(heap_max, (-n, id))
            else:
                print("not cmd")


        empty = False

        flag = False
        while not flag:
            if heap_min:
                min_num ,id = heappop(heap_min)
                flag = validation[id]
            else:
                flag = True
                empty = True


        flag = False
        while not flag:
            if heap_max:
                max_num ,id = heappop(heap_max)
                flag = validation[id]
            else:
                flag = True
                empty = True


        if empty:
            res.append("EMPTY")
        else:
            res.append((-max_num, min_num))


    for r in res:
        if r == "EMPTY":
            print(r)
        else:
            print(r[0], r[1])
    
execute()


