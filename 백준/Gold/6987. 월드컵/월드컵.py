from itertools import combinations
import sys

input = sys.stdin.readline

"""
조건: 
  - 승무패 조건이 한줄로 입력
  
구현:
  - 순열조합을 이용한 백트래킹
  - 주어진 결과에서 15 개의 경기를 진행하며 결과에 맞게 count 를 하나씩 빼면서 확인
"""



def solution(case):
  result = [case[i:i+3] for i in range(0, 16, 3)]
  games = list(combinations(range(6), 2))

  is_possible = False
  def back_track(result, depth):
    nonlocal is_possible
    
    if is_possible:
       return
    if depth == 15:
      if sum(map(sum, result)) == 0:
        is_possible = True
      return
    
    team1, team2 = games[depth]
    for r1, r2 in [(0, 2), (1, 1), (2, 0)]:
      if result[team1][r1] > 0 and result[team2][r2] > 0:
        result[team1][r1] -= 1
        result[team2][r2] -= 1
        back_track(result, depth+1)
        result[team1][r1] += 1
        result[team2][r2] += 1
    
  back_track(result, 0)
  return int(is_possible)

      

# main
case_list = []
for _ in range(4):
  case = list(map(int, input().split()))
  case_list.append(case)

result = []
for case in case_list:
  result.append(solution(case))
print(*result)
  

