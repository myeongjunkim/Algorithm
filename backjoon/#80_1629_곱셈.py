import sys
input=sys.stdin.readline


def multify(A, B, C):
    if B == 1:
        return A%C
    
    else:
        result = multify(A, B//2, C)
        if B%2 == 0:
            return (result*result)%C
        else:
            return (result*result*A)%C


A, B, C = map(int, input().split())

print(multify(A,B,C))