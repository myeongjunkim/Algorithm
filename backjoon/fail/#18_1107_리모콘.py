import sys

N = input('')
T = int(input(''))

if int(N)>100:
    cnt_100 = int(N)-100
else:
    cnt_100 = 100 - int(N)



if T != 0:
    num_list = list(map(int,input('').split(' ')))
    usable_num=list(set([0,1,2,3,4,5,6,7,8,9]) - set(num_list))
    if len(usable_num) == 0:
        print(cnt_100)
        sys.exit(0)
    usable_num.sort()
else:
    print(min(len(N),cnt_100))
    sys.exit(0)



# 고장나지 않은 숫자로 만들 수 있는 가장 가까운 숫자를 찾아냄
# 방법 1 => 큰 자릿수부터 numlist 확인, 큰 숫자를 쓸지 작은 숫자를 쓸지 확인
# 작은거 큰거 구분해서 넣기


digit = len(N)
d = 1
result, cnt = 0, 0
for n in N:
    check_n = int(n)
    if check_n in num_list:
        i=0
        add_num=[]
        while len(add_num) == 0:
            i+=1
            
            ii = 0
            p = 0
            if check_n+i > 9:
                p = -10
                ii =1
            if check_n+i + p not in num_list:
                add_num.append([check_n+i + p, ii, "over"])
            
            ii = 0
            p = 0
            if check_n-i < 0:
                p = 10
                ii = -1
            if check_n-i + p not in num_list:
                add_num.append([check_n-i + p, ii, "under"])
            


        if len(add_num) == 2:
            cnt +=1

            over_result = result + add_num[0][1] *(10**(digit-d+1)) + add_num[0][0] * (10**(digit-d))
            under_result = result + add_num[1][1] *(10**(digit-d+1)) + add_num[1][0] * (10**(digit-d))

            for i in range(digit-d):
                cnt +=1
                over_result += usable_num[0] *(10**(digit-d-i-1))
                under_result += usable_num[-1] *(10**(digit-d-i-1))
            if under_result < 0:
                under_result = 0
            cnt += min(over_result-int(N), int(N)-under_result)
        elif len(add_num) == 1:
            cnt +=1
            result += add_num[0][1] *(10**(digit-d+1)) + add_num[0][0] * (10**(digit-d))
            over_result=0
            under_result=0
            for i in range(digit-d):
                cnt +=1
                over_result += usable_num[0] *(10**(digit-d-i-1))
                under_result += usable_num[-1] *(10**(digit-d-i-1))
            if add_num[0][2] == "over":
                result += over_result
                cnt += result-int(N)

            elif add_num[0][2] == "under":
                result += under_result
                if result < 0:
                    result = 0
                cnt += int(N)-result
        break
        
    else:
        result += check_n * (10**(digit-d))
        cnt +=1

    d +=1

            

print(min(cnt,cnt_100))

