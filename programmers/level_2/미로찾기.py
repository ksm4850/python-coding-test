from collections import deque

def bfs(start,end,maps):
    # 탐색할 방향
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    visited = [[False] * m for __ in range(n)]
    q = deque()
    
    flag = False # 시작점찾는 flag
    
    # 시작점 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i,j,0)) # x, y, cost
                visited[i][j] = True
                flag = True
                break
        if flag: break
    
    while q:
        y,x, cost = q.popleft()
        
                
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny,nx,cost+1))
                    visited[ny][nx] = True
    return -1
    
    
def solution(maps):
    path1 = bfs('S','L',maps) # 시작 - 레버
    path2 = bfs('L','E',maps) # 레버 - 출구
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))