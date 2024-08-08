
# 입력
n = int(input())
m = int(input())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [0] * len(graph)

def dfs(start):
    visited[start] = 1
    
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

dfs(1)

print(sum(visited)-1)