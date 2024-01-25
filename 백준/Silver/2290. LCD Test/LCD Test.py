import sys

input = sys.stdin.readline

"""
조건: 
  - 표시할 n은 문자열 수
  - 가로 s+2, 세로 2s+3
  - 숫자 사이에 간격 필요
구현:
  - 빈 리스트 LCD 를 만든다
  - 정수 n 을 프린팅 포멧(2차원 배열)으로 변환하는 LCD_convertor 를 구현한다.
  - n_str 을 순회하며  LCD_convertor 로 변환한 값을 LCD 에 append 한다
  - 
"""


def solution(s, n_str):
  
  R, C = 2*s+3, s+2
  LCD = [[] for _ in range(R)]
  for n in n_str:
    converted_n = LCD_convertor(n, R, C)
    for r in range(R):
      LCD[r].extend(converted_n[r])
      LCD[r].append(" ")
  
  LCD_printer(LCD)

def LCD_convertor(n, R, C):
  LCD = [[" "]*C for _ in range(R)]
  middle_r = R//2
  top_r, bottom_r = 0, R-1
  
  if n == "1":
    for r in range(R):
      if r not in [top_r, bottom_r, middle_r]:
        LCD[r][-1] = "|"
  elif n == "2":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r:
        LCD[r][-1] = "|"
      elif middle_r<r<bottom_r:
        LCD[r][0] = "|"
  elif n == "3":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      else:
        LCD[r][-1] = "|"
  elif n == "4":
    for r in range(R):
      if r == top_r:
        continue
      elif r == middle_r:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r:
        LCD[r][0] = "|"
        LCD[r][-1] = "|"
      elif middle_r<r<bottom_r:
        LCD[r][-1] = "|"
  elif n == "5":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r:
        LCD[r][0] = "|"
      elif middle_r<r<bottom_r:
        LCD[r][-1] = "|"
  elif n == "6":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r:
        LCD[r][0] = "|"
      elif middle_r<r<bottom_r:
        LCD[r][0] = "|"
        LCD[r][-1] = "|"
  elif n == "7":
    for r in range(R):
      if r == top_r:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r or middle_r<r<bottom_r:
        LCD[r][-1] = "|"
  elif n == "8":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r or middle_r<r<bottom_r:
        LCD[r][0] = "|"
        LCD[r][-1] = "|"
  elif n == "9":
    for r in range(R):
      if r in [top_r, bottom_r, middle_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r:
        LCD[r][0] = "|"
        LCD[r][-1] = "|"
      elif middle_r<r<bottom_r:
        LCD[r][-1] = "|"
  elif n == "0":
    for r in range(R):
      if r in [top_r, bottom_r]:
        LCD[r] = [" "] + ["-"]*(C-2) + [" "]
      elif top_r<r<middle_r or middle_r<r<bottom_r:
        LCD[r][0] = "|"
        LCD[r][-1] = "|"
    
  return LCD


def LCD_printer(LCD):
  for line in LCD:
    line_str = "".join(line)
    print(line_str)
    

# main
s, n_str = input().split()
solution(int(s), n_str)
