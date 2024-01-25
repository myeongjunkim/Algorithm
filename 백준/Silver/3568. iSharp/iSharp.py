import sys

input = sys.stdin.readline

"""
조건: 
  - 각 줄에 변수형과 변수로 선언할 수 있도록 변경하는 함수
  - type 이 주어지고 , 와 ; 으로 변수가 구분됨

구현:
 - 공백으로 split
 - 0인덱스는 타입
 - 1~끝 까지 순회하면서 타입 관련 은 타입에 추가하기
 - 각 변수의 타입과 변수 출력
 - 변수에 타입이 없을 때, 타입이 [] 일때 처리 필요
"""

def solution(line):
  parts = line.split()
  origin_type, origin_vars = parts[0], [ part[:-1] for part in parts[1:] ]

  for origin_var in origin_vars:
    type, var = parse_var(origin_var)
    type = origin_type + "".join(type[::-1])
    print(type, var+";")
  
    
  
def parse_var(origin_var):
  type = []
  var = ""
  for s in origin_var:
    if s == "&":
      type.append("&")
    elif s == "[":
      type.append("[]")
    elif s == "]":
      pass
    elif s == "*":
      type.append("*")
    else:
      var += s
  return type, var
 
 
# main
line = input().strip()
solution(line)