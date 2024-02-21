import sys
from collections import deque

input = sys.stdin.readline

"""
조건:
  - N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)
  - 경사로의 높이는 무조건 1
  
구현:
  - 길이가 L 인 예비 경사로 리스트 업데이트
  - 길이차이가 1 이상인 pos 나오면 False
  - 길이가 1 커진 pos 일 때 예비 경사로 리스트에 있는 숫자가 모두 동일하면 통과
  - 길이가 1 줄어든 pos 일 때 +L 만큼의 리스트가 같은 숫자이면 통과
  
"""

def solution(N, L, _map):

  def check_line(line, L):
    pre_incline = [line[0]]
    i = 1
    while i < N:
      if line[i] == pre_incline[-1]:
        pre_incline.append(line[i])
        i += 1
      elif line[i] == pre_incline[-1]+1 and len(pre_incline) >= L:
        pre_incline = [line[i]]
        i += 1
      elif line[i] == pre_incline[-1]-1 and i+L <= N and len(set(line[i:i+L])) == 1:
        if i+L == N:
          i = i+L
        elif i+L < N:
          if line[i+L] == line[i]:
            pre_incline = [line[i]]
            i = i+L+1
          elif line[i]-line[i+L] == 1:
            pre_incline = [line[i]]
            i = i+L
          else:
            return False
      else:
        return False
      
    return True
      
  
  lines = _map + [ [_map[r][c] for r in range(N)] for c in range(N)]
  result = 0
  for line in lines:
    if check_line(line, L):
      result += 1
  
  
  return result
  
# main
N, L = map(int, input().split())
_map = [ list(map(int, input().split())) for _ in range(N)]
print(solution(N,L, _map))

