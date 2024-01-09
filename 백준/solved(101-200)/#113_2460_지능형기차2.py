import sys

input = sys.stdin.readline


def solution():
  N = 10
  points = [list(map(int, input().split())) for _ in range(N)]

  max_people = 0
  current_people = 0

  for out_p, in_p in points:
    current_people -= out_p
    if current_people > max_people:
      max_people = current_people
    
    current_people += in_p
    if current_people > max_people:
      max_people = current_people

  print(max_people)

solution()