import sys, json
from collections import deque

input = sys.stdin.readline

Test_case = int(input().strip())


answer = []
for i in range(Test_case):
    cmd = input().strip()
    N = int(input().strip())
    arr = json.loads(input().strip())
    
    q = deque(arr)

    flag = 0
    R = False
    for c in cmd:
        if c == 'R':
            R = not R
        elif c == 'D':
            if q:
                if R: q.pop()
                else: q.popleft()
            else:
                flag = 1
                break
    
    if flag:
        answer.append("error")
    else:
        arr = list(q)
        if R: arr.reverse()
        answer.append(json.dumps(arr))

for ret in answer:
    print(ret.replace(" ", ""))
    # if ret != "error":
    #     print("[", end='')
    #     for i in range(len(ret)):
    #         if i == len(ret)-1: print(ret[i], end='')
    #         else : print(ret[i], end=',')
    #     print("]")


