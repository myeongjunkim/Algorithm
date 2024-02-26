import sys
from collections import deque

input = sys.stdin.readline

# 3:32

"""
조건:
  - 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다
  - 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴 회전
    - 극이 다르다면 반대로 회전
  - 12시방향부터 시계방향 순서대로 주어진다
  - 회전 횟수 K(1 ≤ K ≤ 100)
  - 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이
  - -1 이 반시계, 1이 시계
  
구현:
  - q 에 넣고 회전 시킨다.
  - 2번 톱니 - 7번톱니, 2번톱니 - 7번톱니, 2번톱니 - 7번 톱니
  - 각 톱니바퀴의 0번 인덱스로 결과 계산
"""

def solution(wheels, spins):
  
  for n, s in spins:
    w = n-1
    spin_d = [0, 0, 0, 0]

    spin_d[w] = s
    for i in range(w, 0, -1):
      if wheels[i][6] != wheels[i-1][2]:
        spin_d[i-1] = s if (w-(i-1))%2 == 0 else -s
      else:
        break        
    
    for i in range(w, len(wheels)-1):
      if wheels[i][2] != wheels[i+1][6]:
        spin_d[i+1] = s if ((i+1)-w)%2 == 0 else -s
      else:
        break

    for i in range(len(spin_d)):
      if spin_d[i] != 0:
        wheels[i].rotate(spin_d[i])
    
  
  return sum(wheels[i][0] * (2**i) for i in range(len(wheels))) 

        
  
# main
wheels = [ deque(map(int, list(input().strip()))) for _ in range(4)]
K = int(input())
spins = [ list(map(int, input().split())) for _ in range(K) ]
print(solution(wheels, spins))


