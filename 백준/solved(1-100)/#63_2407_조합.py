import sys
input = sys.stdin.readline

def factorial(N):
    sum = 1
    for i in range(1, N+1):
        sum *= i
    return sum

def solution():
    N, M = map(int, input().split())
    result = 1
    for i in range(N, N-M, -1):
        result *=i
    print(result // factorial(M))
    

solution()