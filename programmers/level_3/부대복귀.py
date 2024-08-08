from collections import deque
def solution(n, roads, sources, destination):
    visit = [-1] * (n + 1)
    graph = [[] for _ in range(n+1)]

    # 간선정보
    for s,e in roads:
        graph[s].append(e)
        graph[e].append(s)

    Q = deque([destination])
    visit[destination] = 0
    # 각 부대원 위치에서 출발 bfs
    while Q:
        now = Q.popleft()

        for node in graph[now]:
            if visit[node] == -1: # 방문하지않았으면
                visit[node] = visit[now] + 1 
                Q.append(node)

    return [visit[i] for i in sources]


print(solution(3,[[1,2],[2,3]],[2,3],1))


# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     u, v = map(int,input().split())

#     graph[u].append(v)
#     graph[v].append(u)