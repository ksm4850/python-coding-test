from collections import deque
def solution(maps):
    n = len(maps); m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((0,0))
    visited[0][0] = True

    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    maps[ny][nx] = maps[y][x] + 1

    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

    
"""
n x m 크기
1 <= n,m <= 100
0 벽 
1 벽없
1,1 에서 n,m까지 최단거리 구하기
도착못하는경우 -1
"""
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
