T = int(input(''))

num_list = list(map(int,input('').split(' ')))

cnt = 0
for num in num_list:
    if num != 1:
        if num == 2:
            cnt +=1
        else:
            flag = True
            for i in range(2,num):
                if num % i == 0:
                    flag = False
                    break
            if flag: cnt +=1

print(cnt)