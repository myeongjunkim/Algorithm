
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

N = int(input(''))
result = 0
if N %2 == 0:
    start=0
else:
    start=1

for i in range(start,N+1, 2):
    part_result=1

    for j in range((N - i)//2 + i,(N - i)//2,-1):
        part_result *= j
    result += (2**((N - i)//2)) * part_result // factorial(i)
    
print(result%10007)