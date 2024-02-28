"""
6:14~

조건:
    - 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    - words에 있는 단어로만 변환할 수 있습니다.
    - begin에서 target으로 변환하는 가장 짧은 변환 과정
    - 각 단어의 길이는 3 이상 10 이하, 모든 단어의 길이는 같습니다.
    - words에는 3개 이상 50개 이하의 단어
    - 변환할 수 없는 경우에는 0를 return 합니다.
구현:
    - bfs 를 통해 풀이
        - words 를 순회하면서
        - pos_word 와 한글자 차이인 단어를 인접 노드로 생각
        - 인접노드 중에 방문하지 않은 글자 append

반례:
    - words 에 target 이 없는 경우 0 반환 체크
    - "ssi" 와 같은 단어 조심
"""

from collections import deque

def solution(begin, target, words):
    
    def is_possible(word1, word2):
        w2 = list(word2)
        for i in range(len(word1)):
            w1 = list(word1)
            w1[i] = w2[i]
            if w1 == w2:
                return True
        return False
    
    
    if target not in words:
        return 0
    visited = [False] * len(words)
    q = deque( [(begin, 0)] )
    while q:
        pos_word, d = q.popleft()
        for i in range(len(words)):
            next_word = words[i]
            next_d = d+1
            if visited[i]:
                continue
            if not is_possible(pos_word, next_word):
                continue
            if next_word == target:
                return next_d
            q.append((next_word,next_d))
            visited[i] = True
    
    return 0