import sys

input = sys.stdin.readline


def solution():
  """
  - 피보나치 수열을 행렬의 곱으로 표현한다
    
    F_n_2 = 1 * F_n + 1 * F_n_1
    F_n_1 = 0 * F_n + 1 * F_n_1

    -> (n, n+1) 에 행렬 한번 곱하면 n+2 값 구할 수 있다.
    -> N번째 값 구하기 위해서는 (0, 1) 에 행렬의 n-1 거듭제곱을 하면 된다.
  
  - 분할 정복 방식 함수를 구현한다.
    0. N 이 1 일 때
      -> 그대로 리턴
    1. N 이 짝수일 때
      -> (n-1) // 2 의 값 두개의 곱
    2. N 이 홀수일 때
      -> (n-1) // 2 의 값 두개와 행열 하나의 곱

  - f_matrix 의 n-1 을 거듭제곱한다.
  - 행렬의 [0][0] 값을 구한다.
    
  """
  N = int(input())

  F_matrix = [
    [1,1],
    [1,0]
  ]
  if N == 1:
    print(1)
  else:
    result = power_matrix(F_matrix, N-1)
    print(result[0][0])



def power_matrix(matrix, N):
  if N == 1:
    return matrix

  part_result = power_matrix(matrix, N//2)
  result = mul_matrix(part_result, part_result)
  if N%2 == 0:
    return result
  else:
    return mul_matrix(result, matrix)

def mul_matrix(a, b):
  """행렬의 곱"""
  result_11 = a[0][0]*b[0][0] + a[0][1]*b[1][0]
  result_12 = a[0][0]*b[0][1] + a[0][1]*b[1][1]
  result_21 = a[1][0]*b[0][0] + a[1][1]*b[1][0]
  result_22 = a[1][0]*b[0][1] + a[1][1]*b[1][1]

  return [
    [ result_11%1_000_000_007, result_12%1_000_000_007 ],
    [ result_21%1_000_000_007, result_22%1_000_000_007 ]
  ]

solution()