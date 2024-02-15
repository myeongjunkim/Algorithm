import sys
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건:
  - 서로 다른 L개의 알파벳 소문자들
  - 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
  - 증가하는 순서로 정렬된 문자열
  -  (3 ≤ L ≤ C ≤ 15)
구현:
  - 백트래킹
  - 선택 했을 때 와 안했을 때 각각 탐색
  - L 까지 탐색후 종료
"""

def solution(L, C, chars):
  chars.sort()
  visited = [False] * C
  result = []
  def dfs(depth, length):
    
    if depth >= C:
      if length == L:
        sol_str = "".join([chars[i] for i in range(C) if visited[i]])
        mo = len([c for c in sol_str if c in "aeiou"])
        ja = L - mo
        if mo>=1 and ja>=2:
          result.append(sol_str)
      return
      
    visited[depth] = True
    dfs(depth+1, length+1)
    visited[depth] = False
    dfs(depth+1, length)

  dfs(0, 0)
  return result
  

# main
L, C = map(int, input().split())
chars = list(input().split())
print(*solution(L, C, chars), sep="\n")
