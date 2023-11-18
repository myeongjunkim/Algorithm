"""
x > 0 : push
x== 0 : pop min
"""

import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def save():
    N = int(input())
    cmd = []
    for i in range(N):
        n = int(input())
        cmd.append(n)
    return cmd
    
def execute():
    cmds = save()
    q_min = []
    for n in cmds:
        if n == 0:
            if q_min: print(heappop(q_min))
            else: print(0)
        else:
            heappush(q_min, n)

execute()