def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    for com in range(n):
        if not visited[com]:
            dfs(n,computers,com,visited)
            answer += 1

    return answer

def dfs(n,computers,com,visited):
    visited[com] = True

    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if not visited[connect]:
                dfs(n,computers,connect,visited)

def bfs(n,computers,com,visited):
    visited[com] = True
    q = []
    q.append(com)
    
    while len(q) != 0:
        com = q.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if not visited[connect]:
                    q.append(connect)


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))