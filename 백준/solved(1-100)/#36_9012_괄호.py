import sys
T = int(input(''))

data_list = [sys.stdin.readline().strip() for i in range(T)]

for line in data_list:
    stack=[]
    flag=False
    for c in line:
        if c == '(':
            stack.append(c)
        elif len(stack)==0:
            flag=True
            break
        else:
            stack.pop()
    if len(stack) !=0 or flag:
        print("NO")
    else:
        print("YES")

