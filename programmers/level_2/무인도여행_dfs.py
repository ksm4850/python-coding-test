import sys
sys.setrecursionlimit(int(1e7))
def solution(maps):
    answer = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]    

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    
    def dfs(y,x):
        visited[y][x] = True
        area = int(maps[y][x])

        for dx,dy in directions:
            ny,nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 'X':
                area += dfs(ny,nx)

        return area

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs(i,j))
    if answer:
        return sorted(answer)
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))



