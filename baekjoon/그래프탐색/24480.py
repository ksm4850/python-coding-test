"""
깊이우선탐색 (DFS, Depth-First-Search)
"""
import sys
sys.setrecursionlimit(int(1e6)) # 재귀함수 한계 풀어줌
input = sys.stdin.readline

#입력
n, m, r = map(int, input().split())

# 그래프 그리기
graph = [[] for _ in range(n+1)]   # 정점 0은 버림
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)      # 정점 연결하기
    graph[v].append(u)

for i in range(n+1):    # 오름차순 정렬
    graph[i].sort()

cnt = [0 for _ in range(n+1)]     # 방문 순서 리스트
visited = [False] * len(graph)   # 방문 여부
t = 1   # 방문 순서

def dfs(graph, start, visited): # graph 그래프의 인접리스트,start 현재방문중인 정점, visited 방문여부리스트
    global t
    
    visited[start] = True
    cnt[start] = t  # 시작 정점의 방문 순서는 1
    t += 1
    
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

dfs(graph, r, visited)

for i in range(1, n+1):
    print(cnt[i])