import sys

input = sys.stdin.readline

"""
조건:
  - 

구현:
  - 
"""

def solution(line1, line2):
  dp = [ [0] * (len(line2)+1) for _ in range(len(line1)+1) ] 

  for i in range(1, len(line1)+1):
    for j in range(1, len(line2)+1):
      if line1[i-1] == line2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
  
  return dp[-1][-1]


# main
line1, line2 = input().strip(), input().strip()
print(solution(line1, line2))
