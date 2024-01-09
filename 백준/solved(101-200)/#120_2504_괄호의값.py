import sys

input = sys.stdin.readline


def solution():
  """
  1. () or [] 이면 2, 3 반환
  2. 분할 체크
    2-1. 분할 되면 recursive
    2-2. 분할 안되면 양끝 체크하고 recursive
  """

  line = input().strip()
  if _validation_line(line):
     print(cal_line(line))
  else:
    return print(0)
  
  
def cal_line(line): 
  if line == "()": 
    return 2
  if line == "[]": 
    return 3
  
  stack = []
  for i in range(len(line)):
    if i != 0 and stack == []:
      return cal_line(line[:i]) + cal_line(line[i:])
    elif line[i] in ["(", "["]:
      stack.append(line[i])
    elif line[i] in [")", "]"]:
      stack.pop()
    
  if line[0] == "(":
    return 2*cal_line(line[1:-1])
  elif line[0] == "[":
    return 3*cal_line(line[1:-1])

  
  
    
def _validation_line(line):
  stack = []
  for c in line:
    if c in ["[", "("]:
      stack.append(c)
    elif c == "]":
      if stack == [] or stack.pop() != "[":
        return False
    elif c == ")":
      if stack == [] or stack.pop() != "(":
        return False
    else:
      return False
      
  if stack != []:
    return False
  return True



solution()