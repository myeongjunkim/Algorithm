from sys import stdin

input = stdin.readline

def solution():
  num_list = [ int(input()) for _ in range(int(input())) ]

  for n in num_list:
    str_n = []
    i = 0
    for c in bin(n)[2:][::-1]:
      if c == "1":
        str_n.append(i)
      i += 1
    print(*str_n)
        

solution()