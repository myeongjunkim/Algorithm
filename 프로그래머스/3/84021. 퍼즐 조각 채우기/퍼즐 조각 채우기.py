
"""
조건:
    - 무조건 꽉 채워서 퍼즐 넣기
    - 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개
    - 정사각형 보드
    
구현:
    - 칸별로 그룹바이 하는 메소드
        - 1개 2개는 무조건 매칭
    - 블록/빈칸 리스트 찾는 메소드
        - 블록을 [[가장 왼쪽, 가장 위],,,] 좌표 순으로 정렬
        - bfs 로 탐색
    - 블록 평행이동 메소드
        - 블록을 가장 왼쪽의 가장 위로 평행이동
    - 블록 회전 메소드
        - 블록을 회전하면서 맞으면 개수 추가
        - 가장 왼쪽, 가장 위의 블록 기준
        - 회전: r-dc,  c+dr
        
예외:
    - 
"""
from collections import deque, defaultdict


def solution(game_board, table):
    def bfs(start, board, visited, _type):
        R, C = len(board), len(board[0])
        block = []
        
        visited[start[0]][start[1]] = True
        q = deque( [ start ] )
        while q:
            r, c = q.popleft()
            block.append((r,c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r, new_c = r+dr, c+dc
                if not (0<=new_r<R and 0<=new_c<C):
                    continue
                if visited[new_r][new_c]:
                    continue
                if board[new_r][new_c] != _type:
                    continue
                q.append((new_r, new_c))
                visited[new_r][new_c] = True
        return block
    
    def get_blocks(board, _type):
        R, C = len(board), len(board[0])
        visited = [ [False]*C for _ in range(R) ]
        blocks = defaultdict(list)
        for r in range(R):
            for c in range(C):
                if not visited[r][c] and board[r][c] == _type:
                    block = bfs((r,c), board, visited, _type)
                    blocks[len(block)].append(block)
        return blocks
    
    
    def rotate(block):
        rotated_block = []
        center_r, center_c = block[0]
        for r, c in block:
            dr, dc = r-center_r, c-center_c
            new_r, new_c = center_r-dc, center_c+dr
            rotated_block.append((new_r, new_c))
        return rotated_block
    
    def move(block):
        moved_block = []
        dr, dc = min(r for r, c in block),  min(c for r, c in block)
        for r, c in block:
            new_r, new_c = r-dr, c-dc
            moved_block.append((new_r, new_c))
        return moved_block
        
    def check_block(space, block):
        for r, c in block:
            if (r,c) not in space:
                return False
        return True
        
        
    
    blocks = get_blocks(table, 1)
    spaces = get_blocks(game_board, 0)
    moved_spaces = { l:  [ move(sp) for sp in space_list ] for l, space_list in spaces.items() }

    result = 0
    visited_spaces = { l: [False]*len(space_list) for l, space_list in spaces.items()}
    for l, l_blocks in blocks.items():
        if l not in moved_spaces:
            continue
        if l < 3:
            result += l*min(len(moved_spaces[l]), len(l_blocks))
        else:
            for block in l_blocks:
                is_possible = False
                for _ in range(4):
                    block = move(block)
                    for i, space in enumerate(moved_spaces[l]):
                        if visited_spaces[l][i]:
                            continue
                        if check_block(block, space):
                            visited_spaces[l][i]=True
                            is_possible = True
                            break
                    if is_possible:
                        break
                    else:
                        block = rotate(block)
                if is_possible:
                    result += l
                          
    return result