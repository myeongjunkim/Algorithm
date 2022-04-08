import random, time

def get_matrix(M, N):
    answer = []
    for i in range(M):
        line = []
        for j in range(N): 
            line.append(random.randrange(0,10))
        answer.append(line)
    return answer

def print_matrix(matrix):
    for line in matrix:
        print(line)

def multify_matrix(matrix1, matrix2):
    answer = [ len(matrix2[0])*[0] for i in range (len(matrix1)) ]
    for i in range (len(answer) ):
        for j in range ( len(answer[i]) ):
            for k in range ( len(matrix1[i] ) ):
                answer[i][j] += matrix1[i][k] * matrix2[k][j]
    return answer

#strassen_idea 내에서 사용
def split_matrix(matrix):
    a11, a12, a21,a22 = [], [], [], []
    M, N = len(matrix), len(matrix[0])
    for i in range(M):
        if i < M/2:
            a11.append(matrix[i][:N//2])
            a12.append(matrix[i][N//2:])
        else:
            a21.append(matrix[i][:N//2])
            a22.append(matrix[i][N//2:])
    return a11, a12, a21, a22


def sum_matrix(A,B): 
    answer = [] 
    for i in range(len(A)): 
        line=[] 
        for j in range(len(A[i])): 
            line.append(A[i][j]+B[i][j]) 
        answer.append(line) 
    return answer

def minus_matrix(A,B): 
    answer = [] 
    for i in range(len(A)): 
        line=[] 
        for j in range(len(A[i])): 
            line.append(A[i][j]-B[i][j]) 
        answer.append(line) 
    return answer

    

def strassen_idea(matrix1, matrix2):
    result_M = len(matrix1)
    a11, a12, a21, a22 = split_matrix(matrix1)
    b11, b12, b21, b22 = split_matrix(matrix2)

    P1 = multify_matrix(a11, minus_matrix(b12, b22))
    P2 = multify_matrix(sum_matrix(a11, a12), b22)
    P3 = multify_matrix(sum_matrix(a21, a22), b11)
    P4 = multify_matrix(a22, minus_matrix(b21, b11))
    P5 = multify_matrix(sum_matrix(a11, a22), sum_matrix(b11, b22))
    P6 = multify_matrix(minus_matrix(a12, a22), sum_matrix(b21, b22))
    P7 = multify_matrix(minus_matrix(a11, a21), sum_matrix(b11, b12))

    r = sum_matrix(minus_matrix(sum_matrix(P5, P4), P2), P6)
    s = sum_matrix(P1, P2)
    t = sum_matrix(P3, P4)
    u = minus_matrix(minus_matrix(sum_matrix(P5, P1), P3), P7)

    # 병합
    answer = []
    for i in range(result_M):
        if i<result_M//2:
            answer.append(r[i]+s[i])
        else:
            answer.append(t[i-result_M//2]+u[i-result_M//2])

    return answer

# main
matrix1, matrix2 = get_matrix(300,100), get_matrix(100, 500)

start = time.time()
origin_case = multify_matrix(matrix1, matrix2)
end = time.time()
origin_case_time = end-start

start = time.time()
strassen_case = strassen_idea(matrix1, matrix2)
end = time.time()
strassen_case_time = end-start

if origin_case == strassen_case:
    print("origin case : " + str(origin_case_time))
    print("strassen case : " + str(strassen_case_time))









    