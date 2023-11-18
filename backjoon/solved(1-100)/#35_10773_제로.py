import sys

T = int(input(''))
num_list = [int(sys.stdin.readline().strip()) for i in range(T)]

result=[]
for n in num_list:
    if n == 0:
        result.pop()
    else:
        result.append(n)
    
print(sum(result))