import sys

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result


def get_case(num):
    cnt = 0
    cnt_3 = num // 3
    for i in range(cnt_3+1):
        rest_num = num - i*3
        cnt_2 = rest_num // 2
        for j in range(cnt_2+1):
            k = rest_num - j*2
            cnt += factorial(i+j+k)//factorial(i)//factorial(j)//factorial(k)

    return cnt

    
N = int(input(''))
result=[]
for i in range(N):
    num = int(sys.stdin.readline().strip())

    cnt = get_case(num)
    result.append(cnt)



for r in result:
    print(r)