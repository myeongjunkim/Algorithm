import sys

input = sys.stdin.readline

N, M = map(int, input().split())


gragh = []
for i in range (M):
    line = input().strip()
    line_list=[]
    for c in line:
        line_list.append(c)
    gragh.append(line_list)


visited=[]
for i in range(M):
    visited.append([False]*N)



cnt = 1
def dfs(gragh, pos, visited):
    r, c = pos[0], pos[1]
    visited[r][c] = True
    global cnt
    if r > 0 and (not visited[r-1][c]):
        if gragh[r][c] == gragh[r-1][c]:
            cnt +=1
            dfs(gragh, [r-1, c], visited)
    
    if r < M-1 and (not visited[r+1][c]):
        if gragh[r][c] == gragh[r+1][c]:
            cnt +=1
            dfs(gragh, [r+1, c], visited)

    if c > 0 and (not visited[r][c-1]):
        if gragh[r][c] == gragh[r][c-1]:
            cnt +=1
            dfs(gragh, [r, c-1], visited)
        
    
    if c < N-1 and (not visited[r][c+1]):
        if gragh[r][c] == gragh[r][c+1]:
            cnt +=1
            dfs(gragh, [r, c+1], visited)



W=[]
B=[]
for r in range(M):
    for c in range(N):
        if not visited[r][c]:
            cnt = 1
            dfs(gragh, [r,c], visited)
            if gragh[r][c] == 'W': W.append(cnt)
            elif gragh[r][c] == 'B': B.append(cnt)



sum_W = 0
for n in W:
    sum_W += n**2

sum_B = 0
for n in B:
    sum_B += n**2

print(sum_W, sum_B)