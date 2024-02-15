import sys
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건:
  - 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면 나쁜수열
  - N은 1 이상 80 이하이다.
  - 가장 작은 좋은 수열
구현:
  - N 까지 depth 가면서
  - 자기 자신과 다른 나머지 두개 경우 체크
  - answer 라는 전역 리스트 관리. 체크하고 다시 원위치로
"""

def solution(N):

  answer = []
  result = []
  def back_tracking():
    if result:
      return
    if len(answer) == N:
      result.append("".join(list(map(str, answer))))
      return
    
    for n in [1,2,3]:
      answer.append(n)
      for i in range(1, len(answer)//2+1):
        if answer[-i-i:-i] == answer[-i:]:
          break
      else:  
        back_tracking()
      answer.pop()

  back_tracking()
  return result[0]

# main
N = int(input())
print(solution(N))
