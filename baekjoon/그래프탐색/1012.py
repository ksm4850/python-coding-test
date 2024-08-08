import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6)) # 재귀함수 한계 풀어줌



def dfs(x,y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    if array[x][y] == 1:
        array[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

t = int(input())
for _ in range(t):
    # 가로 세로 배추개수
    m,n,k = map(int,input().split())
    array = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int, input().split())

        array[y][x] = 1 #  배추 심어져있는곳
    
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)

