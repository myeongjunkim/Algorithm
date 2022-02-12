import sys

T = int(input(''))

num_list = [int(sys.stdin.readline().strip()) for i in range(T)]

i = 1
stack = []
result=[]
flag=True
for num in num_list:
    if i>num:
        if len(stack) == 0 or stack[-1] != num:
           flag = False
           break
        else:
            pop_num = stack.pop()
            result.append("-")
    else:
        stack = stack + list(range(i,num+1))
        result = result + ['+']*(num-i+1)
        i = num+1
        # while num not in stack:
        #     i +=1
        #     stack.append(i)
        #     result.append("+")
        pop_num = stack.pop()
        result.append("-")
        

   

        

if flag:
    for _ in result:
        print(_)
else:
    print("No")