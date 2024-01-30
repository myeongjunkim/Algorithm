import sys

input = sys.stdin.readline

"""
조건: 
  - 0 -> "." // 1 -> "#"
  - 숫자와 숫자 사이에는 1열 이상의 공백이 있다
  - N 은 10만, 5의 배수
  
구현:
  - column 으로 구조화 해서 세로로 한줄씩 읽고 숫자 인식하도록 구현
"""


def solution(N, signal):
  C = N//5

  signal_row = [ 
    signal[:C], signal[C:2*C], signal[2*C:3*C], signal[3*C:4*C], signal[4*C:] 
  ]

  signal_column = []
  for i in range(C):
    column = []
    for signal in signal_row:
      column.append(signal[i])
    signal_column.append("".join(column))

  return read_signal(signal_column)



def read_signal(signal_column):
  C = len(signal_column)

  result = []
  pass_count = 0
  for i in range(C):
    if pass_count:
      pass_count -= 1
      continue
    
    one_flag = False
    if signal_column[i] == "#####":
      if i == C-1 or signal_column[i+1] == ".....":
        result.append("1")
        one_flag = True
      elif signal_column[i+1] == "#...#":
        result.append("0")
      elif signal_column[i+2] == "#.###":
        result.append("6")
      elif signal_column[i+2] == "#####":
        result.append("8")
      else:
        print("error")
    elif signal_column[i] == "#.###":
      result.append("2")
    elif signal_column[i] == "#.#.#":
      result.append("3")
    elif signal_column[i] == "###..":
      result.append("4")
    elif signal_column[i] == "###.#":
      if signal_column[i+2] == "#.###":
        result.append("5")
      elif signal_column[i+2] == "#####":
        result.append("9")
      else:
        print("error")
    elif signal_column[i] == "#....":
      result.append("7")
    else:
      continue

    pass_count = 1 if one_flag else 3
    
    
  
  return result
    

# main
N, signal = int(input()), input().strip()
result = solution(N, signal)
print("".join(result))
