import sys

input = sys.stdin.readline

"""
조건: 
  - BOJ거리의 각 보도블록에는 B, O, J 중에 하나
  - 1번은 반드시 B
  - i+1번부터 N번까지로 점프
  - k칸 점프시 필요한 에너지양 k*k
  - N 은 1000
  - B, O, J, B, O, J, B, O, J, ... 순서로
  - 만날 수 없는 경우에는 -1
  
구현:
  - B, O, J 인덱스 저장
  - N 만큼 순회하면서 이전 칸 조사
    - dp 에 에너지 미니멈 저장
  

"""



def solution(N, line):
  pre_node = { "B":"J", "O":"B", "J":"O" }
  
  dp = [0]
  for i in range(1, N):

    energy = []
    for j in range(i):
      if line[j] != pre_node[line[i]]:
        continue
      if dp[j] < 0:
        continue
      E = dp[j] + (i-j)**2
      energy.append(E)
    dp.append(min(energy) if energy else -1)

  return dp[-1]

# main
N = int(input())
line = input().strip()
print(solution(N, line))


