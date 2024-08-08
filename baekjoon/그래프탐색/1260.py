from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
# 그래프 그리기
for _ in range(1,m+1):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

print(graph)

for i in graph:
    i.sort()

print(graph)

# dfs 함수
def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    
# bfs 함수
def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]: # 방문햇는지
                visited[i] = True
                q.append(i)

# 출력
visited = [False] * len(graph)
dfs(v)
print()
visited = [False] * len(graph)
bfs(v)