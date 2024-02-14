import sys

input = sys.stdin.readline

"""
조건:
  - 길이는 100 이하
  - 중위표기식 -> 후위표기식
  - 알파벳 대문자와 +, -, *, /, (, )
구현:
  - * 와 / 를 괄호로 묶는 과정 구현
  - 괄호 stack과 연산자 stack, 피연산자 stack 관리
    - ) 괄호가 나오면 연산자에서 1개, 피연산자에서 2개 꺼내 순서대로 조합하여 피연산자 스택에 넣기
  - 마지막에 스택에 있는 요소들 털기
"""

def solution(line):
  item_s, op_s = [], []
  for i in range(len(line)):
    if line[i] in "+-*/":
      op_s.append(line[i])
    elif line[i] == "(":
      item_s.append(line[i])
      op_s.append(line[i])
    else:
      if line[i] == ")":
        op, item = op_s.pop(), item_s.pop()
        new_op_s, new_item_s = [], []
        while op != "(":
          new_op_s.append(op)
          op = op_s.pop()
        while item != "(":
          new_item_s.append(item)
          item = item_s.pop()
        while new_op_s:
          op = new_op_s.pop()
          item1, item2 = new_item_s.pop(), new_item_s.pop()
          part = f"{item1}{item2}{op}"
          new_item_s.append(part)
        item_s.append(new_item_s.pop())
      else:
          item_s.append(line[i])

      if op_s and op_s[-1] in "*/":
        item2, item1, op = item_s.pop(), item_s.pop(), op_s.pop()
        part = f"{item1}{item2}{op}"
        item_s.append(part)
    
    # print(i)
    # print(item_s)
    # print(op_s)
    # print()
  
  new_op_s, new_item_s = [], []
  while op_s and op_s[-1] != "(":
    new_op_s.append(op_s.pop())
  while item_s and item_s[-1] != "(":
    new_item_s.append(item_s.pop())
  while new_op_s:
    # print(new_item_s)
    # print(new_op_s)
    # print()
    op = new_op_s.pop()
    item1, item2 = new_item_s.pop(), new_item_s.pop()
    part = f"{item1}{item2}{op}"
    new_item_s.append(part)
  return new_item_s.pop()
  

# main
line = input().strip()
print(solution(line))
