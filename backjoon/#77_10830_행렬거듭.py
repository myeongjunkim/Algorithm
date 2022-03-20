from hashlib import new
import sys
input= sys.stdin.readline

N, cnt = map(int, input().split())

matrix=[]
for i in range(N):
    matrix.append(list(map(int,input().split())))



def square_matrix(matrix):
    new_matrix = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for t in range(N):
                new_matrix[i][j] += matrix[i][t] * matrix[t][j]
            new_matrix[i][j] %= 1000
    return new_matrix

def multi_matrix(matrix1, matrix2):
    new_matrix = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for t in range(N):
                new_matrix[i][j] += matrix1[i][t] * matrix2[t][j]
            new_matrix[i][j] %= 1000
    return new_matrix


def multify(matrix, cnt):

    if cnt == 1:
        return matrix

    result = multify(matrix, cnt//2)
    if cnt %2 == 0:
        return square_matrix(result) 
    else:
        return multi_matrix(square_matrix(result), matrix)

    
    

    

new_matrix = multify(matrix, cnt)
# new_matrix = square_matrix(matrix)


for line in new_matrix:
    output=''
    for c in line:
        output += str(c%1000)+" "
    print(output[:-1])