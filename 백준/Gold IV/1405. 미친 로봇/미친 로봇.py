import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
조건:
  - N 번 움직였을 때 경로들 중 동일 지점을 한번만 방문한 확률
  - 각 방향으로 갈 확률이 주어짐
  - N 은 14 이하
구현:
  - 이차원 평면을 위한 배열 -> visited 관리
  - visited 가능한 곳만 탐방.
  - 가능 경로를 모두 저장
  - 각 확률 모두 더하기
"""

def solution(dist, rates):
  E, W, S, N = rates
  visited = [[False]*(2*dist+1) for _ in range(2*dist+1)]
  visited[0][0] = True
  result = []
  def back_tracking(x, y, depth, rate):
    if depth == dist:
      result.append(rate)
      return

    for dx, dy, new_rate in [(0,1,E), (0,-1,W), (-1,0,S), (1,0,N)]:
      new_x, new_y = x+dx, y+dy
      if visited[new_x][new_y]:
        continue
      visited[new_x][new_y] = True
      back_tracking(new_x, new_y, depth+1, rate*new_rate/100)
      visited[new_x][new_y] = False

  back_tracking(0,0,0,1)
  return sum(result)

# main
line = list(map(int,input().split()))
dist, rates = line[0], line[1:]
print(solution(dist, rates))
