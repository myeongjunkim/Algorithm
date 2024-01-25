import sys

input = sys.stdin.readline

"""
조건: 
  - 어셈블리어를 보고 주어진 규칙에 따라 기계어로 변환하는 어셈블러 코드 작성
구현:
  - opcode 구하기
    C 를 통한 4번 값 처리
    -> rB or #C 결정
    -> 15번 값 결정
  - 5번 값 0 추가
  - rA 000 인 것 분기 처리
  - 
"""

OPCODE = {
  "ADD"  : "0000", 
  "SUB"  : "0001", 
  "MOV"  : "0010",
  "AND"  : "0011",
  "OR"   : "0100",
  "NOT"  : "0101",
  "MULT" : "0110",
  "LSFTL": "0111",
  "LSFTR": "1000",
  "ASFTR": "1001",
  "RL"   : "1010",
  "RR"   : "1011",
}


def solution(line):
  
  opcode, registers = line[0], [ int(r) for r in line[1:] ]
  rD = _convert_to_bin(registers[0], 3)
  rA = _convert_to_bin(registers[1], 3)
  rB = _convert_to_bin(registers[2], 3)
  C = _convert_to_bin(registers[2], 4)
  
  index_0_to_3 = OPCODE[opcode] if opcode[-1] != "C" else OPCODE[opcode[:-1]]
  index_4 = "0" if opcode[-1] != "C" else "1"
  index_5 = "0"
  index_6_to_8 =  rD
  index_9_to_11 = "000" if index_0_to_3 in ["0010", "0101"] else rA
  index_12_to_15 = rB + "0" if index_4 == "0" else C
  
  return index_0_to_3+index_4+index_5+index_6_to_8+index_9_to_11+index_12_to_15
 
def _convert_to_bin(n, length):
  bin_str = str(bin(n))[2:]
  padding = length-len(bin_str)
  return "0"*padding+bin_str

# main
N = int(input())
lines = [input().split() for _ in range(N)]
for line in lines:
  print(solution(line))