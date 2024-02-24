def solution(n, lost, reserve):
    
    lost, reserve = sorted(lost), sorted(reserve)
    visited = [False] * len(reserve)
    
    new_lost = []
    for s in lost:
        possible = False
        for i in range(len(reserve)):
            if s == reserve[i]:
                visited[i] = True
                possible = True
                break
        if not possible:
            new_lost.append(s)
                
    
    for s in new_lost:
        possible = False
        for i in range(len(reserve)):
            if not visited[i] and reserve[i] in [s-1,s+1]:
                visited[i] = True
                possible = True
                break
        if not possible:
            n-=1
    
                
    return n