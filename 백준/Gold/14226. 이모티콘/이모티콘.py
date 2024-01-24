import sys
from collections import deque

input = sys.stdin.readline

"""
조건: 
  - N은 목표 이모티콘
  - 복사, 붙여넣기, 삭제
    - 복사는 현재 개수에 영향을 주지 않지만 시간 1 소요
  - S는 목표값 1000 이하
  
구현:
  - 최단거리 이므로 bfs 사용
  - 3가지 경우를 next_node 로 설정
  - 1차원 배열의 visited 이용
  - 노드는 pos 와 clip_board 로 구성
    clip_board 또한 각 노드마다 다르므로 전역 관리 x

"""

def solution(N):

  visited = [0] * 2001
  is_copy = [False] * 2001

  q = deque([[1, 0, 0]])
  
  while q:
    pos, clip_board, time = q.popleft()
    visited[pos] = True
    if pos == N:
      return time
    
    if pos > 1 and not visited[pos-1]:
      q.append( [pos-1, clip_board, time+1] )
    
    if clip_board and pos < 1001 and not visited[pos+clip_board]:
      q.append( [pos+clip_board, clip_board, time+1] )
      
    if not is_copy[pos]:
      q.append( [pos, pos, time+1] )
      is_copy[pos] = True
    
  return -1



# main
S = int(input())
print(solution(S))