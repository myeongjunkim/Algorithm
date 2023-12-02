import sys

input = sys.stdin.readline


def solution():
  """
  [조건 정리]
  - 멀티탭 구멍: N
  - 총 사용: K
  - 사용하려면 플러그에 연결되어있어야함
  [예시 정리]
  - 2 3 2 3 1 2 7
    2번, 3번 꼽기
    1번 사용할 때 3번 빼고 1번 꼽기 ( 2번이 뒤에서 사용하므로 )
    7번 사용할 때 1번 or 2번 빼고 꼽기 ( 마지막이므로 아무거나 )
  [풀이 정리]
  - 콘센트 리스트
  - 사용 리스트 순회
    - in 콘센트 리스트
      있으면 pass
      없으면 콘센트 리스트 순회하여 사용빈도가 적은 것 뽑기, count 증가
  """
  N, K = map(int, input().strip().split())
  use_list = input().split()
  plug_in = []

  count = 0
  for i in range(K):
    if use_list[i] not in plug_in:
      if len(plug_in) < N: 
        plug_in.append(use_list[i])
      else:
        pop_plugin = find_pop_plugin(plug_in, use_list[i:])
        
        plug_in.remove(pop_plugin)
        plug_in.append(use_list[i])
        count += 1
  
  print(count)


def find_pop_plugin(plug_in, use_list):
  max_index = 0
  max_p = plug_in[0]
  for p in plug_in:
    if p not in use_list:
      return p
    for i in range(len(use_list)):
      if p == use_list[i]: 
        if i > max_index:
          max_index, max_p = i, p
        break
  return max_p
        

solution()

