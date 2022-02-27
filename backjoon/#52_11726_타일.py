N = int(input(''))

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

if N%2 ==0:
    start = 0
else:
    start = 1

result = 0
for i in range(start, N+1, 2):
    square = (N - i)//2
    result += factorial(i+square)//factorial(square)//factorial(i)

print(result%10007)