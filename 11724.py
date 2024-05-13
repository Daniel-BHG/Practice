# DFS -> if end, cnt += 1
# Next, unvisited note

N, M = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]

graph = [[0 for _ in range(N)] for _ in range(N)]
# egde[0][0] - edge[0][1], edge[1][0] - edge[1][1]
for i in range(M):
    graph[edge[i][0]][edge[i][1]] = 1
    graph[edge[i][1]][edge[i][0]] = 1
print(graph)
visited = [False] * N

def dfs(row):
    # 1. Visited
    visited[row] = True

    # 2. Next
    for i in range(N):
        if visited[i] == False and graph[]