import sys
input = sys.stdin.readline

T = int(input())

num_list = [int(input().strip()) for i in range(T)]

i= 1
stack = []
result = []
flag = True
for num in num_list:
   
    while i <= num:
        stack.append(i)
        result.append("+")
        i +=1
        
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False       
        


if flag:
    for _ in result:
        print(_)
else:
    print("NO")