# 입력
n = int(input())
m = int(input())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (len(graph))

def dfs(start):
    