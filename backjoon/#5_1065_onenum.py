N = int(input(''))
cnt = 0
for n in range(1,N+1):
    num_list = []
    while n !=0:
        num_list.append(n%10)
        n = n//10
    if len(num_list)>1:
        d = num_list[1]-num_list[0]
    else:
        d = 0
    flag = True
    for i in range(len(num_list)):
        if num_list[i] != (num_list[0] + i*d):
            flag = False
            break
    if flag:
        cnt +=1

print(cnt)