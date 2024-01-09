def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def comb(m,n):
    if m-n < n:
        n = m-n
    result = 1
    for i in range(n):
        result *= (m-i)
    return int(result / factorial(n))


cnt = int(input(''))
result = []
for i in range(cnt):
    n_m = input().split(' ')

    N = int(n_m[0])
    M = int(n_m[1])

    result.append(comb(M, N))
    
for i in result:
    print(i)
