
import sys
input = sys.stdin.readline

from heapq import heappop, heappush


def save():
    N = int(input())
    cmd = []
    for i in range(N):
        n = int(input())
        cmd.append(n)
    return cmd

def execute():
    heap=[]
    cmds = save()
    for n in cmds:
        if n == 0:
            if heap:
                print(heappop(heap)[1])
            else: print(0)
        else:
            heappush(heap, (-n, n))

execute()