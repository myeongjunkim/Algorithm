
#https://thought-process-ing.tistory.com/m/269

from itertools import combinations
import sys

input = sys.stdin.readline


def solution():
  """
  - 단어는 N개, 글자수 K개
  - "anta", "tica"
    -> a:3, t:2, c:1, n:1, i:1
    -> K 가 5 미만: 0개
    -> K 가 5 이상:
      - can = K - 5
      - have = {a, t, c, n, i}
      - need = set(word[4:-4]) - have
  - 0개 ~ can개 추가 했을 때
    최대가 되도록 하는 알파벳 모두 찾기
      case 1 일 때
      case 2 일 때
      ,,,
        
  """
  N, K = map(int, input().split())
  word_list = [ input().strip()[4:-4] for line in range(N) ]
  char_list = { chr(i) for i in range(97, 123) } - {"a", "t", "c", "n", "i"}
  if K < 5:
    print(0)
  else:
    result = solve_using_combinatoin(word_list, char_list, K-5)
    print(result)
    


def solve_using_combinatoin(word_list, char_list, n):
  max_count = 0
  for case in combinations(char_list, n):
    count = 0
    learned = get_learned(case)
    for word in word_list:
      if is_read(word, learned):
        count += 1
    max_count = max(max_count, count)
  return max_count

def get_learned(case):
  learned = [False] * 26
  for c in case:
    learned[ord(c)-97] = True
  for c in {"a", "t", "c", "n", "i"}:
    learned[ord(c)-97] = True
  return learned


def is_read(word, learned):
  for w in word:
    if not learned[ord(w)-97]:
      return False
    else:
      pass
  return True



solution()




# 백트랙킹 접근법
def find_max_count(have: set, can: int, word_list, result):
  global max_count, visited_word_list

  if not word_list:
    return

  for word in word_list:
    needs = set(word) - have
    if len(needs) <= can:
      new_word_list = set(word_list) - {word}
      if visited_word_list & new_word_list:
        return
      visited_word_list.add(new_word_list)
      find_max_count(have|needs, can-len(needs), new_word_list, result+1)
    else:
      max_count = max(max_count , result)
      print(result)