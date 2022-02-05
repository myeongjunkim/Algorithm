def fibo(N):
    if N == 0:
        print(1,0)
    else:
        last_num = 0
        num = 1
        for i in range(N-1):
            next_num = last_num + num
            last_num = num
            num = next_num
        print(last_num, num)

T = int(input(''))

num_list=[]
for i in range(T):
    num_list.append(int(input('')))

for num in num_list:
    fibo(num)

