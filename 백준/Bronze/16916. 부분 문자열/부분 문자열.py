import sys
from collections import deque

input = sys.stdin.readline


"""
조건: 
  - 문자열 길이 100만 
  
구현:
  - 문자열 인덱스를 통해 구현
  
"""

def solution(all_str, part_str):
  for i, s in enumerate(all_str):
    if s == part_str[0] and all_str[i:i+len(part_str)] == part_str:
      return 1
  return 0
  

# main
all_str = input().strip()
part_str = input().strip()
print(1 if all_str.find(part_str) >= 0 else 0)
# print(solution(all_str, part_str))

      