import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

"""
조건:
  - 사람에게 번호를 1부터 N까지로 배정
  - i번 사람과 j번 사람 -> 팀에 더해지는 능력치는 Sij와 Sji
  - N(4 ≤ N ≤ 20, N은 짝수)
  
구현:
  Team1, Team2 로 지정하기
  - N 의 절반 인덱스를 combination 으로 구한다.
  - 나머지 절반 인덱스를 구한다.
  
    - 절반 인덱스에서 2 개를 combination 으로 구한다.
      Sij + Sji 를 합산한다.
    - 나머지 절반 인덱스에서 2 개를 combination 으로 구한다.
      Sij + Sji 를 합산한다.
      
  - 차이를 업데이트 한다.
  
  
"""

def solution(N, _map):

  min_result = sys.maxsize
  for TEAM1 in combinations(range(N), N//2):
    TEAM2 = [ n for n in range(N) if n not in TEAM1 ]

    result_1 = 0
    for A,B in combinations(TEAM1, 2):
      result_1 += (_map[A][B]+_map[B][A])

    result_2 = 0
    for A,B in combinations(TEAM2, 2):
      result_2 += (_map[A][B]+_map[B][A])

    min_result = min(min_result, abs(result_1-result_2))

  return min_result

# main
N = int(input())
_map = [ list(map(int, input().split())) for _ in range(N)]
print(solution(N, _map))
