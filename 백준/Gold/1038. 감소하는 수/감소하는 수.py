import sys
from itertools import combinations

input = sys.stdin.readline

"""
조건: 
  - N 번째 감소수, N 은 백만
  - 최대 감소수 : 9876543210
  
구현:
  - 9~0 범위에서 자리수별 조합을 사용
"""


def solution(N):
  if N<10:
    return N

  count = 9
  for i in range(2,11):
    nums = []
    for case in combinations("9876543210", i):
      nums.append("".join(case))
    
    if count + len(nums) < N:
      count += len(nums)
    elif count + len(nums) == N:
      return int(nums[0])
    else:
      for k in range(len(nums)-1, -1, -1):
        count += 1
        if count == N:
          return int(nums[k])
  return -1

    

# main
N = int(input())
print(solution(N))

      