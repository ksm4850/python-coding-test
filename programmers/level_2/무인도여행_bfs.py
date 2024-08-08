from collections import deque
def solution(maps):
    answer = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]    

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque()
                area = int(maps[i][j])
                q.append((i,j))

                visited[i][j] = True

                while q:
                    x,y = q.popleft()

                    for dx,dy in directions:
                        nx,ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            area += int(maps[nx][ny])
                            q.append((nx,ny))
                            visited[nx][ny] = True

                answer.append(area)
    if answer:
        return sorted(answer)
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))



